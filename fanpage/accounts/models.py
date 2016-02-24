from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):


	user = models.OneToOneField(User, primary_key=True)
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	profile_pic = models.ImageField(upload_to='images',null=True, blank=True)
	favorite_song = models.CharField(max_length=128, blank=True)
	favorite_album = models.CharField(max_length=32, blank=True)
	about = models.TextField()

	def save(self, *args, **kwargs):
		"""Override save to increment user_id by 1"""
		if self.user_id is None:
			self.user_id =  self.__class__.objects.all().order_by("-user_id")[0].user_id + 1
			return super(self.__class__, self).save(*args, **kwargs)

	def __str__(self):
		"""Prettify output"""
		return "{} {}".format(self.first_name, self.last_name)