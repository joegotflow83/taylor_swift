from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):


	user = models.OneToOneField(User)
	profile_pic = models.ImageField(upload_to='images',null=True, blank=True)
	favorite_song = models.CharField(max_length=128)
	favorite_album = models.CharField(max_length=32)
	about = models.TextField()