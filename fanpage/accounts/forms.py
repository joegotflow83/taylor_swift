from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserForm(forms.ModelForm):


	class Meta:


		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password',
				  'last_login', 'date_joined']


class UserProfileForm(forms.ModelForm):


	class Meta:


		model = UserProfile
		fields = ['favorite_song', 'favorite_album', 'about']