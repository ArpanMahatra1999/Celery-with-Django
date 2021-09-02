from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.contrib import rdb

import time


@shared_task
def sum(a,b):
    time.sleep(10)
    return a+b


@shared_task
def send_email(email):
    time.sleep(10)
    rdb.set_trace()
    print(f"The mail is send to {email}")