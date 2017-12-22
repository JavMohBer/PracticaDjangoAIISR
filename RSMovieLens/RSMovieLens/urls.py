#encoding:utf-8
from django.conf.urls import *
from django.contrib import admin
from main.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^$', index),
    url(r'^populate', populateDB),
    url(r'^loadRS', loadRS),
    url(r'^search', search),
    url(r'^recommendedFilms', recommendedFilms),
    url(r'^similarFilms', similarFilms),
    #url(r'^admin/doc/', include(django.contrib.admindocs.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

