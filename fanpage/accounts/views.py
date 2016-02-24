from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import UserProfile
from .forms import UserForm, UserProfileForm, ProfilePicForm


class Register(FormView):


	template_name = 'accounts/register.html'
	form_class = UserForm
	fields = ['username', 'email', 'password1', 'password2',
			  'first_name', 'last_name']
	success_url = '/accounts/login/'

	def form_valid(self, form):
		"""validate the form"""
		user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password1'])
		user.save()
		return super().form_valid(form)


class AuthLogin(View):


	def post(self, request):
		"""Allow a user to log in"""
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/accounts/set_profile/')
		else:
			return HttpResponse('Invalid Credentials')

	def get(self, request):
		"""Display the log in form for the user"""
		return render(request, 'accounts/login.html')


class Profile(DetailView):


	queryset = UserProfile.objects.all()

	def get_object(self):
		"""Display the users profile info"""
		object = super().get_object()
		return object


class SetProfile(FormView):


	template_name = 'accounts/set_profile.html'
	form_class = UserProfileForm
	success_url = '/'

	def form_valid(self, form):
		"""Validate the form"""
		new_profile = UserProfile.objects.create(
								first_name=form.cleaned_data['first_name'],
								last_name=form.cleaned_data['last_name'],
								favorite_song=form.cleaned_data['favorite_song'],
								favorite_album=form.cleaned_data['favorite_album'],
								about=form.cleaned_data['about'])
		new_profile.save()
		return super().form_valid(form)


class UpdateProfile(UpdateView):


	model = UserProfile
	fields = ['favorite_song', 'favorite_album', 'about']
	template_name = 'accounts/update_profile.html'
	success_url = '/'

	def get_object(self, queryset=None):
		"""Grab the correct users info"""
		return self.request.user

	def form_valid(self, form):
		"""Validate the form"""
		return super().form_valid(form)


class UpdateProfilePic(UpdateView):


	model = UserProfile
	fields = ['profile_pic']
	template_name = 'accounts/updatepic.html'
	success_url = '/'

	def get_object(self, queryset=None):
		"""Grab the correct user to update pic"""
		return self.request.user

	def form_valid(self, form):
		"""Validate the form"""
		return super().form_valid(form)


class AuthLogout(View):


	def get(self, request):
		"""Log the user out"""
		logout(request)
		return redirect('/')