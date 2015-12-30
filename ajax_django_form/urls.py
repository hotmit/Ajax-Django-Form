from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^human/', include('ajax_django_form.human.urls', namespace='human'))
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]

