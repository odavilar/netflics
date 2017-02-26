from django.conf.urls import url

from . import views

app_name = 'mynetflix'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^search/', views.search_movie, name='search_movie'),
]

