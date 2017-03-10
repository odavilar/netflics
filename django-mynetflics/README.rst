=====
My Netflics
=====

My Netflics is a simple Django app to browse movies.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "mynetflics" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'mynetflics',
    ]

2. Include the mynetflics URLconf in your project urls.py like this::

	url(r'^', include('mynetflics.urls')), #default to movies
    url(r'^movie/', include('mynetflics.urls')),

3. Run `python manage.py migrate` to create the mynetflics models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a movie (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/mynetflics/ to browse movies.