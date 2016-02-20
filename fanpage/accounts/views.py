from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from .forms import UserForm, UserProfileForm


class Register:


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