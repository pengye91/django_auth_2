#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# author: xyp
from __future__ import unicode_literals
from django.conf.urls import url
from .views import home, show_color, set_color

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^show_color/$', show_color, name='show_color'),
    url(r'^set_color/$', set_color, name='set_color'),
]
