# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, View
from django.http import JsonResponse, HttpResponse
from movie.models import Movie
from django.core import serializers


class MovieListView(ListView):
    model = Movie
    # print(object_list)
    def get_queryset(self, **kwargs):
        print("Run")
        # serializers.serialize("json", self.object_list)
        return super().get_queryset()

    def get(self, request, *args, **kwargs):
        return HttpResponse(serializers.serialize('json', self.get_queryset()))



class MovieView(View):
    model = Movie
    success_url = '/movie_list'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        m = Movie.objects.create(title=request.REQUEST['title'])
        m.save()
        return HttpResponse(status=201)

    def patch(self, request, *args, **kwargs):
        movie = Movie.objects.get(id=kwargs['pk'])
        movie.title = request.REQUEST['title']
        movie.save()
        return HttpResponse(status=200)

    def delete(self, request, *args, **kwargs):
        movie = Movie.objects.get(id=kwargs['pk'])
        movie.delete()
        return HttpResponse(status=200)



class MovieDetailView(DetailView):
    model = Movie

    def get(self, request, *args, **kwargs):
        print(self.get_object())
        return HttpResponse(serializers.serialize('json', [self.get_object()]))
        # return JsonResponse(self.get_object(), safe=False)
