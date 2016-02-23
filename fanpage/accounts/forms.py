from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

from .models import UserProfile


class UserForm(UserCreationForm):


	email = forms.EmailField(required=True)


	class Meta:


		model = User
		fields = ['username', 'email', 'password1', 'password2']
		last_login = forms.DateTimeField(datetime.datetime.now())
		date_joined = forms.DateTimeField(datetime.datetime.now())

		def save(self, commit=True):
			"""Override save method to save data to User model"""
			data = self.cleaned_data
			user = User(email=data['email'])
			user.save()


class UserProfileForm(forms.ModelForm):


	class Meta:


		model = UserProfile
		fields = ['first_name', 'last_name', 'favorite_song', 
				  'favorite_album', 'about']


class ProfilePicForm(forms.ModelForm):


	class Meta:


		model = UserProfile
		fields = ['profile_pic']