from django.conf.urls import include, url
from django.contrib import admin

from movie_api.views import hello, MovieListCreate, MovieDeleteUpdateDetail

urlpatterns = [

    url(r'^hello/', hello),
    url(r'^movie/$', MovieListCreate.as_view(), name='movie'),
    url(r'^movie/(?P<pk>\d+)/$', MovieDeleteUpdateDetail.as_view(), name='movie_dud'),

]