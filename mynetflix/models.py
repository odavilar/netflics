from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    synopsis = models.TextField(max_length=200)
    poster = models.URLField()
    trailer = models.URLField()
    clasification = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)

    def __str__(self):
        return self.title

    def get_awards(self):
        return list(self.movieaward_set.values_list('award__award_name',flat=True))

    def get_actors(self):
        return list(self.movieactor_set.values_list('actor',flat=True))

    def get_genres(self):
        return list(self.moviegenre_set.values_list('genre',flat=True))

    def get_directors(self):
        return list(self.moviedirector_set.values_list('director',flat=True))

@python_2_unicode_compatible
class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.CharField(max_length=200)

    def __str__(self):
        return self.actor

@python_2_unicode_compatible
class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre

@python_2_unicode_compatible
class MovieDirector(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.CharField(max_length=200)

    def __str__(self):
        return self.director

class Award(models.Model):
    award_name = models.CharField(max_length=200)
    academy = models.CharField(max_length=200)

    def __str__(self):
        return self.academy + " - " + self.award_name

@python_2_unicode_compatible
class MovieAward(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)

    def __str__(self):
        return self.award.award_name