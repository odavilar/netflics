from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Movie, Actor, Genre, Director, Award
from .forms import SearchForm

class IndexView(generic.ListView):
    template_name = 'mynetflix/index.html'
    model = Movie
    context_object_name = 'movie_list'

    def get_queryset(self):
        """Return movies ordered by title."""
        return Movie.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        return context

class DetailView(generic.DetailView):
    model = Movie
    template_name = 'mynetflix/detail.html'
