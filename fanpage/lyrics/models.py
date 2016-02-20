from django.db import models


class Lyrics(models.Model):

	
	author = models.CharField(max_length=15)
	album = models.CharField(max_length=40)
	song = models.CharField(max_length=128)
	lyrics = models.TextField()

	def __str__(self):
		"""Prettify output of song"""
		return self.song