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
		fields = ['first_name', 'last_name', 'profile_pic', 'favorite_song', 
				  'favorite_album', 'about']

		def save(self, commit=True):
			"""Override the save method to save data to user profile"""
			user = UserProfileForm(self.cleaned_data['first_name'],
								   self.cleaned_data['last_name'],
								   self.cleaned_data['profile_pic'],
								   self.cleaned_data['favorite_song'],
								   self.cleaned_data['favorite_album'],
								   self.cleaned_data['about'])
			user.save()


class UpdateProfileForm(forms.ModelForm):


	class Meta:


		model = UserProfile
		fields = ['favorite_song', 'favorite_album', 'about']

		def save(self, commit=True):
			"""Update the users profile info"""
			profile = UserProfile(self.cleaned_data['favorite_song'],
								  self.cleaned_data['favorite_album'],
								  self.cleaned_data['about'])
			profile.save()


class ProfilePicForm(forms.ModelForm):


	class Meta:


		model = UserProfile
		fields = ['profile_pic']

		def save(self, commit=True):
			"""Update the user profile picture"""
			profile_pic = UserProfileForm(self.cleaned_data['profile_pic'])
			profile_pic.save()