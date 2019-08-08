# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    print(111)
    return x + y


@shared_task
def mul(x, y):
    print(222)
    return x * y


@shared_task
def xsum(numbers):
    print(333)
    return sum(numbers)
