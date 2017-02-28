from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import Min
from .models import Movie, MovieActor, MovieGenre, MovieDirector, MovieAward
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
                data_output = list(data_output.values_list('title',flat=True))
                data_output = joinby(data_output, ', ')
                return HttpResponse("Movie results %s." % data_output)

            if type_to_search == SearchForm.DIRECTOR:
                data_output = MovieDirector.objects.filter(director__icontains=data_to_search)
                data_output = list(data_output.values_list('director',flat=True))
                data_output = joinby(data_output, ', ')
                return HttpResponse("Director results %s." % data_output)

            if type_to_search == SearchForm.COUNTRY:
                data_output = Movie.objects.filter(country__icontains=data_to_search)
                data_output = list(data_output.values_list('country',flat=True))
                data_output = joinby(data_output, ', ')
                return HttpResponse("Country results %s." % data_output)

            if type_to_search == SearchForm.PRICES:
                data_output = MovieAward.objects.filter(award__award_name__icontains=data_to_search)
                data_output = list(data_output.values_list('award__award_name',flat=True))
                data_output = joinby(data_output, ', ')
                return HttpResponse("Award results %s." % data_output)

            if type_to_search == SearchForm.ACTOR:
                data_output = MovieActor.objects.filter(actor__icontains=data_to_search)
                data_output = list(data_output.values_list('actor',flat=True))
                data_output = joinby(data_output, ', ')
                return HttpResponse("Actor results %s." % data_output)

    # if a GET (or any other method) we'll create a blank form
    return HttpResponseRedirect('/')