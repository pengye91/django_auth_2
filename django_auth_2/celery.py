#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# author: xyp
from __future__ import unicode_literals, absolute_import

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTING_MODULE', 'django_auth_2.settings')

app = Celery('django_auth_2')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
