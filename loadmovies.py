import csv
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

from mynetflix.models import Movie, Actor, Genre, Director, Country

with open('peliculas.txt', 'rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    for row in tsvin:
        country1=Country(row[8])
        country1.save()
        m = Movie(title=row[0], year=row[1], synopsis=row[9], poster=row[7], trailer=row[6], clasification=row[3], country=country1)
        m.save()
        director1=Director(row[2])
        director1.save()
        m.moviedirector_set.create(director=Director(row[2]))
        genre_data = row[4].split(',')
        for genre in genre_data:
            genre1=Genre(genre.strip())
            genre1.save()
            m.moviegenre_set.create(genre=Genre(genre.strip()))
            print genre
        actor_data = row[5].split(',')
        for actor in actor_data:
            actor1=Actor(actor.strip())
            actor1.save()
            m.movieactor_set.create(actor=Actor(actor.strip()))
            print actor