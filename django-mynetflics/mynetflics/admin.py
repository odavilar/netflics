from django.contrib import admin

# Register your models here.
from .models import Movie, MovieActor, MovieGenre, MovieDirector, MovieAward, Award, Actor, Genre, Director, Country

class ActorInline(admin.TabularInline):
    model = MovieActor
    extra = 3

class GenreInline(admin.TabularInline):
    model = MovieGenre
    extra = 3

class DirectorInline(admin.TabularInline):
    model = MovieDirector
    extra = 2

class AwardInline(admin.TabularInline):
    model = MovieAward
    extra = 3

class MovieAdmin(admin.ModelAdmin):
    inlines = [DirectorInline, ActorInline, GenreInline, AwardInline]

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieActor)
admin.site.register(MovieGenre)
admin.site.register(MovieDirector)
admin.site.register(MovieAward)
admin.site.register(Award)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Country)
