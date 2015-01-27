from django.conf.urls import patterns, url
from notify import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^register/$', views.register, name='register'),
		url(r'^confirm/$', views.confirm, name='confirm'),
)