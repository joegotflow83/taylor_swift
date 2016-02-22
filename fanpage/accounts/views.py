from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import UserProfile
from .forms import UserForm, UserProfileForm, ProfilePicForm


class Register(ListView):


	def post(self, request):
		"""Allow a user to register"""
		uf = UserForm(request.POST, prefix='user')
		upf = UserProfileForm(request.POST, prefix='userprofile')
		if uf.is_valid() * upf.is_valid():
			new_user = User.objects.create_user(**uf.cleaned_data)
			login(new_user)
			userprofile = upf.save(commit=False)
			userprofile.user = new_user
			userprofile.save()
			return redirect('/')
		else:
			uf.errors
			upf.errors

	def get(self, request):
		"""Display forms for user to fill out"""
		uf = UserForm(prefix='user')
		upf = UserProfileForm(prefix='userprofile')
		return render(request, 'accounts/register.html', 
								{'userform': uf,
								'userprofileform': upf},
								context_instance=RequestContext(request))


class AuthLogin(ListView):


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


	def get(self, request):
		"""Display the users profile info"""
		user = User.objects.get(id=1)
		profile = UserProfile.objects.get(id=1)
		return render(request, 'accounts/profile.html', {'profile': profile,
														 'user': user})


class UpdateProfilePic(ListView):


	def post(self, request):
		"""Allow a user to update their profile pic"""
		form = ProfilePicForm(request.POST, request.FILES, prefix='profilepic')
		if form.is_valid():
			form.save(commit=True)
			return redirect('/accounts/')
		else:
			form.errors

	def get(self, request):
		"""Display the form to update their picture"""
		form = ProfilePicForm()
		return render(request, 'accounts/updatepic.html', {'form': form})


class AuthLogout(ListView):


	def get(self, request):
		"""Log the user out"""
		logout(request)
		return redirect('/')