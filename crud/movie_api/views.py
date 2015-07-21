from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from rest_framework import generics
from movie.models import Movie
from rest_framework import serializers
# Create your views here.

def hello(request):
    pass


class Movie_Serializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(method_name='make_url')

    def make_url(self, request):
        return reverse_lazy('movie_dud', kwargs={'pk':request.id})

    class Meta:
        model = Movie
        fields = ['title', 'url']

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer


class MovieDeleteUpdateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer