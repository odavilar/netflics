import csv
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

from mynetflix.models import Movie, Actor, Genre, Director, Country

with open('peliculas.txt', 'rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    for row in tsvin:
        country1=Country(country=row[8])
        try:
            country1.save()
        except:
            print "already exists"
        m = Movie(title=row[0], year=row[1], synopsis=row[9], poster=row[7], trailer=row[6], clasification=row[3], country=Country.objects.get(country__iexact=country1.country))
        m.save()
        director1=Director(director=row[2])
        try:
            director1.save()
        except:
            print "already exists"
        m.moviedirector_set.create(director=Director.objects.get(director__iexact=director1.director))
        genre_data = row[4].split(',')
        for genre in genre_data:
            genre1=Genre(genre=genre.strip())
            try:
                genre1.save()
            except:
                print "already exists"
            m.moviegenre_set.create(genre=Genre.objects.get(genre__iexact=genre1.genre))
            print genre
        actor_data = row[5].split(',')
        for actor in actor_data:
            actor1=Actor(actor=actor.strip())
            try:
                actor1.save()
            except:
                print "already exists"
            m.movieactor_set.create(actor=Actor.objects.get(actor__iexact=actor1.actor))
            print actor