from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


from .forms import UserForm, UserProfileForm


class Register(ListView):


	def post(self, request):
		"""Allow a user to register"""
		uf = UserForm(request.POST, prefix='user')
		upf = UserProfileForm(request.POST, prefix='userprofile')
		if uf.is_valid() * upf.is_valid():
			user = uf.save()
			userprofile = upf.save(commit=False)
			userprofile.user = user
			userprofile.save()
			return redirect('/')

	def get(self, request):
		"""Display forms for user to fill out"""
		uf = UserForm(prefix='user')
		upf = UserProfileForm(prefix='userprofile')
		return render_to_response('accounts/register.html', 
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


class AuthLogout(ListView):


	def get(self, request):
		"""Log the user out"""
		logout(request)
		return redirect('/')