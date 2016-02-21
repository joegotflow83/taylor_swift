from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Lyrics


class SongsList(ListView):


   model = Lyrics


class SongDetail(DetailView):


	queryset = Lyrics.objects.all()
	template_name = 'lyrics/song.html'

	def get_object(self):
		"""When user clicks on song display all info about the song"""
		object = super(SongDetail, self).get_object()
		return object
		