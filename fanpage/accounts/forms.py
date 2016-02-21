from django import forms
from django.contrib.auth.models import User
import datetime

from .models import UserProfile


class UserForm(forms.ModelForm):


	class Meta:


		model = User
		fields = ['username', 'email', 'password', 'first_name', 'last_name']
		last_login = forms.DateTimeField(datetime.datetime.now())
		date_joined = forms.DateTimeField(datetime.datetime.now())


class UserProfileForm(forms.ModelForm):


	class Meta:


		model = UserProfile
		fields = ['favorite_song', 'favorite_album', 'about']