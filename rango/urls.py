#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Fanxu Meng
# All rights reserved (C) 2019 by Fanxu Meng

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
]