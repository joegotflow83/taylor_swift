from django.shortcuts import render, redirect
from django.views.generic import ListView, View
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
	success_url = '/accounts/update_profile/'

	def form_valid(self, form):
		"""validate the form"""
		valid = super().form_valid(form)
		username, password = form.cleaned_data.get('username'), \
							 form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return valid


class AuthLogin(View):


	def post(self, request):
		"""Allow a user to log in"""
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return HttpResponse('Invalid Credentials')

	def get(self, request):
		"""Display the log in form for the user"""
		return render(request, 'accounts/login.html')


class Profile(ListView):


	def get(self, request, pk):
		"""Display the users profile info"""
		user = User.objects.get(pk=pk)
		profile = UserProfile.objects.get(pk=pk)
		return render(request, 'accounts/profile.html', {'profile': profile,
														 'user': user})

class UpdateProfile(ListView):


	def post(self, request):
		"""Allow the user to update their profile information"""
		form = UserProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('/accounts')
		else:
			form.errors

	def get(self, request):
		"""Display profile form"""
		form = UserProfileForm
		return render(request, 'accounts/update_profile.html', {'form': form})


class UpdateProfilePic(ListView):


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