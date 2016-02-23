from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import FormView
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
			return redirect('/accounts/update_profile/')
		else:
			return HttpResponse('Invalid Credentials')

	def get(self, request):
		"""Display the log in form for the user"""
		return render(request, 'accounts/login.html')


class Profile(DetailView):


	model = UserProfile

	def get_context_data(self, **kwargs):
		"""Display the users profile info"""
		object = super().get_context_data()
		return object


class UpdateProfile(FormView):


	template_name = 'accounts/update_profile.html'
	form_class = UserProfileForm
	success_url = '/accounts/'

	def form_valid(self, form):
		"""Validate the form"""
		profile = UserProfile(form.cleaned_data['first_name'],
						   form.cleaned_data['last_name'],
						   form.cleaned_data['favorite_song'],
						   form.cleaned_data['favorite_album'],
						   form.cleaned_data['about'])
		profile.save()
		return super().form_valid(form)


class UpdateProfilePic(View):


	def post(self, request):
		"""Allow a user to update their profile pic"""
		form = ProfilePicForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return redirect('/accounts/')
		else:
			form.errors

	def get(self, request):
		"""Display the form to update their picture"""
		form = ProfilePicForm()
		return render(request, 'accounts/updatepic.html', {'form': form})


class AuthLogout(View):


	def get(self, request):
		"""Log the user out"""
		logout(request)
		return redirect('/')