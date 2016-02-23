from django.views.generic import TemplateView
import tweepy
import wikipedia

from fanpage import settings

# import twitter api keys
auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_secret)
api = tweepy.API(auth)

class Index(TemplateView):


	template_name = 'main/index.html'
		

class About(TemplateView):

	
	def get_context_data(self):
		"""Display about page"""
		context = super().get_context_data()
		context = wikipedia.page('Taylor Swift')
		return context


class TwitterFeed(TemplateView):


	def get_context_data(self):
		context = super().get_context_data()
		context = api.user_timeline(screen_name='taylorswift13')
		return context
		
