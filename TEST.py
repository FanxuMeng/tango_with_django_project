#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Fanxu Meng
# All rights reserved (C) 2019 by Fanxu Meng

python_pages = [
    {'title': 'Official Python Tutorial',
     'url': 'http://docs.python.org/3/tutorial/',
     'views': 4},
    {'title': 'How to Think like a Computer Scientist',
     'url': 'http://www.greenteapress.com/thinkpython/',
     'views': 5},
    {'title': 'Learn Python in 10 Minutes',
     'url': 'http://www.korokithakis.net/tutorials/python/',
     'views': 6}]

django_pages = [
    {'title': 'Official Django Tutorial',
     'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
     'views': 7},
    {'title': 'Django Rocks',
     'url': 'http://www.djangorocks.com/',
     'views': 8},
    {'title': 'How to Tango with Django',
     'url': 'http://www.tangowithdjango.com/',
     'views': 9}]

other_pages = [
    {'title': 'Bottle',
     'url': 'http://bottlepy.org/docs/dev/',
     'views': 10},
    {'title': 'Flask',
     'url': 'http://flask.pocoo.org',
     'views': 11}]

cats = {
    'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
    'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
    'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
}

for cat, cat_data in cats.items():
    print(cat)
    print(cat_data)
    print(cat_data['likes'])
    #c = add_cat(cat, cat_data['likes'], cat_data['views'])
    for p in cat_data['pages']:
        print(p['views'])
        #add_page(c, p['title'], p['url'], p['views'])
