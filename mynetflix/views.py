from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from django.db.models import Min
from .models import Movie, Actor, Award, Director, Country
from .forms import SearchForm
from mynetflix.templatetags.mynetflix_extras import joinby
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from collections import OrderedDict

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

class FormView(generic.FormView):
    template_name = 'mynetflix/index.html'
    form_class = SearchForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(SearchForm, self).form_valid(form)

    def get_queryset(self):
        """Return movies ordered by title."""
        return Movie.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        context['movie_list'] = Movie.objects.order_by('-pub_date')[:5]
        return context

def search_movie(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data_to_search = form.cleaned_data['search_text']
            type_to_search = form.cleaned_data['search_by']

            if type_to_search == SearchForm.TITLE:
                data_output = Movie.objects.filter(title__icontains=data_to_search)
                data_output = list(data_output)
                context = {'search_type':'movie', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

            if type_to_search == SearchForm.DIRECTOR:
                data_output = Director.objects.filter(director__icontains=data_to_search)
                data_output = list(data_output)
                context = {'search_type':'director', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

            if type_to_search == SearchForm.COUNTRY:
                data_output = Country.objects.filter(country__icontains=data_to_search)
                data_output = list(data_output)
                context = {'search_type':'country', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

            if type_to_search == SearchForm.PRICES:
                data_output = Award.objects.filter(award_name__icontains=data_to_search)
                data_output = list(data_output)
                context = {'search_type':'award', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

            if type_to_search == SearchForm.ACTOR:
                data_output = Actor.objects.filter(actor__icontains=data_to_search)
                data_output = list(data_output)
                context = {'search_type':'actor', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

    # if a GET (or any other method) we'll create a blank form
    return HttpResponseRedirect('/')

def MovieListbyActor(request, data):
    data_output = list(Movie.objects.filter(movieactor__actor__id=data))
    x = Actor.objects.get(pk=data)
    context = {'title':x.actor, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyAward(request, data):
    data_output = list(Movie.objects.filter(movieaward__award__id=data))
    x = Award.objects.get(pk=data)
    context = {'title':x.award_name, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyDirector(request, data):
    data_output = list(Movie.objects.filter(moviedirector__director__id=data))
    x = Director.objects.get(pk=data)
    context = {'title':x.director, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyCountry(request, data):
    data_output = list(Movie.objects.filter(country__id=data))
    x = Country.objects.get(pk=data)
    context = {'title':x.country, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyActorSlug(request, data):
    data = data.replace("-"," ")
    data = data.title()
    data_output = list(Movie.objects.filter(movieactor__actor__actor=data))
    context = {'title':data, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyAwardSlug(request, data):
    data = data.replace("-"," ")
    data_output = list(Movie.objects.filter(movieaward__award__award_name__iexact=data))
    context = {'title':data, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyDirectorSlug(request, data):
    data = data.replace("-"," ")
    data = data.title()
    data_output = list(Movie.objects.filter(moviedirector__director__director=data))
    context = {'title':data, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyCountrySlug(request, data):
    data_output = list(Movie.objects.filter(country__country__iexact=data))
    context = {'title':data, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieApi(request, data):
    data = data.replace("-"," ")
    data = data.title()
    data_output = Movie.objects.get(title__iexact=data)
    title = data_output.title
    year = data_output.year
    synopsis = data_output.synopsis
    poster = data_output.poster
    trailer = data_output.trailer
    country = data_output.country.country
    clasification = data_output.clasification
    awards = ', '.join(data_output.get_awards())
    directors = ', '.join(data_output.get_directors())
    actors = ', '.join(data_output.get_actors())
    genres = ', '.join(data_output.get_genres())
    data = OrderedDict()
    data['title'] = title
    data['year'] = year
    data['synopsis'] = synopsis
    data['poster'] = poster
    data['trailer'] = trailer
    data['country'] = country
    data['clasification'] = clasification
    data['directors'] = directors
    data['actors'] = actors
    data['genres'] = genres
    data['awards'] = awards
    json_data = json.dumps(data)
    #serialized_q = json.dumps(list(data_output), cls=DjangoJSONEncoder)
    return HttpResponse(json_data,content_type = "application/json")

def ActorApi(request, data):
    data = data.replace("-"," ")
    data = data.title()
    data_output = Movie.objects.filter(movieactor__actor__actor=data)
    json_data = serializers.serialize('json', data_output)
    return HttpResponse(json_data,content_type = "application/json")

def DirectorApi(request, data):
    data = data.replace("-"," ")
    data = data.title()
    data_output = Movie.objects.filter(moviedirector__director__director=data)
    json_data = serializers.serialize('json', data_output)
    return HttpResponse(json_data,content_type = "application/json")

def AwardApi(request, data):
    data = data.replace("-"," ")
    data = data.title()
    data_output = Movie.objects.filter(movieaward__award__award_name=data)
    json_data = serializers.serialize('json', data_output)
    return HttpResponse(json_data,content_type = "application/json")

def CountryApi(request, data):
    data = data.replace("-"," ")
    data = data.title()
    data_output = Movie.objects.filter(country__country__iexact=data)
    json_data = serializers.serialize('json', data_output)
    return HttpResponse(json_data,content_type = "application/json")