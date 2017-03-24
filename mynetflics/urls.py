from django.conf.urls import url

from . import views

app_name = 'mynetflics'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^search/', views.search_movie, name='search_movie'),
    url(r'^actor/(?P<data>[\w-]+)/', views.MovieListbyActor, name='actor'),
    url(r'^award/(?P<data>[\w-]+)/', views.MovieListbyAward, name='award'),
    url(r'^director/(?P<data>[\w-]+)/', views.MovieListbyDirector, name='director'),
    url(r'^country/(?P<data>[\w-]+)/', views.MovieListbyCountry, name='country'),
    url(r'^actor/(?P<data>[\w-]+)/', views.MovieListbyActorSlug, name='actor'),
    url(r'^award/(?P<data>[\w-]+)/', views.MovieListbyAwardSlug, name='award'),
    url(r'^director/(?P<data>[\w-]+)/', views.MovieListbyDirectorSlug, name='director'),
    url(r'^country/(?P<data>[\w-]+)/', views.MovieListbyCountrySlug, name='country'),
    url(r'^api/movie/(?P<data>[\w-]+)/', views.MovieApi, name='movieapi'),
    url(r'^api/actor/(?P<data>[\w-]+)/', views.ActorApi, name='actorapi'),
    url(r'^api/award/(?P<data>[\w-]+)/', views.AwardApi, name='awardapi'),
    url(r'^api/director/(?P<data>[\w-]+)/', views.DirectorApi, name='directorapi'),
    url(r'^api/country/(?P<data>[\w-]+)/', views.CountryApi, name='countryapi'),
    url(r'^movie/(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),
]

