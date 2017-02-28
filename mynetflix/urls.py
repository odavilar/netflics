from django.conf.urls import url

from . import views

app_name = 'mynetflix'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^search/', views.search_movie, name='search_movie'),
    url(r'^actor/(?P<data>[\w-]+)/', views.MovieListbyActor, name='actor'),
    url(r'^award/(?P<data>[\w-]+)/', views.MovieListbyAward, name='award'),
    url(r'^director/(?P<data>[\w-]+)/', views.MovieListbyDirector, name='director'),
    url(r'^country/(?P<data>[\w-]+)/', views.MovieListbyCountry, name='country'),
]

