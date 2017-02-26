from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    synopsis = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    trailer = models.CharField(max_length=200)
    clasification = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)

    def __str__(self):
        return self.title

    def get_awards(self):
        return list(self.award_set.values_list('award',flat=True))

    def get_actors(self):
        return list(self.actor_set.values_list('actor',flat=True))

    def get_genres(self):
        return list(self.genre_set.values_list('genre',flat=True))

    def get_directors(self):
        return list(self.director_set.values_list('director',flat=True))

@python_2_unicode_compatible
class Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.CharField(max_length=200)

    def __str__(self):
        return self.actor

@python_2_unicode_compatible
class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre

@python_2_unicode_compatible
class Director(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.CharField(max_length=200)

    def __str__(self):
        return self.director

@python_2_unicode_compatible
class Award(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    award = models.CharField(max_length=200)

    def __str__(self):
        return self.award
