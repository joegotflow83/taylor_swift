from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

from .models import UserProfile


class UserForm(UserCreationForm):


	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length = 32)
	last_name = forms.CharField(max_length = 32)


	class Meta:


		model = User
		fields = ['username', 'email', 'password1', 'password2',
				  'first_name', 'last_name']
		last_login = forms.DateTimeField(datetime.datetime.now())
		date_joined = forms.DateTimeField(datetime.datetime.now())

		def save(self, commit=True):
			"""Override save method to save data to User model"""
			data = self.cleaned_data
			user = User(email=data['email'], first_name=data['password1'],
			last_name=data['password2'], password1=data['first_name'],
			password2=data['last_name'])
			user.save()


class UserProfileForm(forms.ModelForm):


	class Meta:


		model = UserProfile
		fields = ['favorite_song', 'favorite_album', 'about']


class ProfilePicForm(forms.ModelForm):


	class Meta:


		model = UserProfile
		fields = ['profile_pic']