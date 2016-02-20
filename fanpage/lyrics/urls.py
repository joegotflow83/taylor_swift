from django.conf.urls import url

from lyrics import views

urlpatterns = [
	url(r'^$', views.SongsList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.SongDetail.as_view(), name='detail'),	
]