from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import Min
from .models import Movie, Actor, Award, Director, Country
from .forms import SearchForm
from mynetflix.templatetags.mynetflix_extras import joinby

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
                data_output = list(data_output.values_list('director',flat=True))
                context = {'search_type':'director', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

            if type_to_search == SearchForm.COUNTRY:
                data_output = Country.objects.filter(country__icontains=data_to_search)
                data_output = list(data_output.values_list('country',flat=True))
                context = {'search_type':'country', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

            if type_to_search == SearchForm.PRICES:
                data_output = Award.objects.filter(award_name__icontains=data_to_search)
                data_output = list(data_output.values_list('award_name',flat=True))
                context = {'search_type':'award', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

            if type_to_search == SearchForm.ACTOR:
                data_output = Actor.objects.filter(actor__icontains=data_to_search)
                data_output = list(data_output.values_list('actor',flat=True))
                context = {'search_type':'actor', 'results': data_output}
                return render(request, 'mynetflix/results.html', context)

    # if a GET (or any other method) we'll create a blank form
    return HttpResponseRedirect('/')

def MovieListbyActor(request, data):
    data = data.replace("-"," ")
    data = data.title()
    data_output = list(Movie.objects.filter(movieactor__actor=data))
    context = {'title':data, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyAward(request, data):
    data = data.replace("-"," ")
    data_output = list(Movie.objects.filter(movieaward__award__award_name__iexact=data))
    context = {'title':data, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyDirector(request, data):
    data = data.replace("-"," ")
    data_output = list(Movie.objects.filter(moviedirector__director__iexact=data))
    context = {'title':data, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)

def MovieListbyCountry(request, data):
    data_output = list(Movie.objects.filter(country__country__iexact=data))
    context = {'title':data, 'results': data_output}
    return render(request, 'mynetflix/movielistby.html', context)