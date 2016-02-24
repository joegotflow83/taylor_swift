"""fanpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin

from .settings import MEDIA_ROOT
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^songs/', include('lyrics.urls')),
    url(r'^twitter/$', TemplateView.as_view(template_name="main/twitter.html"), name='twitter'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^media/(?P<path>.*)/$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
]
