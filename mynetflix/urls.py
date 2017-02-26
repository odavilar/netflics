from django.conf.urls import url

from . import views

app_name = 'mynetflix'
urlpatterns = [
    url(r'^$', views.FormView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

