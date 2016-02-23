from django.conf.urls import url

from accounts import views


urlpatterns = [
	url(r'^register/$', views.Register.as_view(), name='register'),
	url(r'^login/$', views.AuthLogin.as_view(), name='login'),
	url(r'^update_profile/$', views.UpdateProfile.as_view(), name='update_profile'),
	url(r'^update_profile_picture/$', views.UpdateProfilePic.as_view(), name='update_pic'),
	url(r'^$', views.Profile.as_view(), name='profile'),
	url(r'^logout/$', views.AuthLogout.as_view(), name='logout'),
]