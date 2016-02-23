from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):


	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	profile_pic = models.ImageField(upload_to='images',null=True, blank=True)
	favorite_song = models.CharField(max_length=128, blank=True)
	favorite_album = models.CharField(max_length=32, blank=True)
	about = models.TextField()

	def __str__(self):
		"""Prettify output"""
		return "{} {}".format(self.first_name, self.last_name)