from django.shortcuts import render
from django.views.generic import ListView, TemplateView
import tweepy

from fanpage import settings

# import twitter api keys
auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_secret)
api = tweepy.API(auth)

class Index(ListView):


	def get(self, request):
		"""Direct users to home page"""
		return render(request, 'main/index.html')	

class About(TemplateView):


	template_name = 'main/about.html'


class TwitterFeed(ListView):


	def get(self, request):
		"""Grap Taylors tweets"""
		user = api.get_user('taylorswift13')
		timeline = api.user_timeline(screen_name='taylorswift13')
		return render(request, 'main/twitter.html', 
					 {'user': user,
					  'timeline': timeline})
