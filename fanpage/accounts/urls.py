from django.conf.urls import url

from accounts import views


urlpatterns = [
	url(r'^register/$', views.Register.as_view(), name='register'),
	url(r'^login/$', views.AuthLogin.as_view(), name='login'),
	url(r'^logout/$', views.AuthLogout.as_view(), name='logout'),
]