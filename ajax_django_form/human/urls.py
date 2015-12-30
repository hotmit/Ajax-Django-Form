from django.conf.urls import url
from . import views


urlpatterns =  [
    url(r'^$', views.list_human, name='view_human'),
    url(r'^create/$', views.create_human, name='create_user'),
    url(r'^update/$', views.update_human, name='update_user'),
]