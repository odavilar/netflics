# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 06:52
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=200, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='actor', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=200)),
                ('academy', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='award_name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='country', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=200, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='director', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=200, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='genre', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('synopsis', models.TextField(max_length=200)),
                ('poster', models.URLField()),
                ('trailer', models.URLField()),
                ('clasification', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Country')),
            ],
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Award')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Director')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynetflics.Movie')),
            ],
        ),
    ]
