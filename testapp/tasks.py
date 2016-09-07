#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# author: xyp
from __future__ import unicode_literals, absolute_import
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
