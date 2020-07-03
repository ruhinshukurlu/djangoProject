from __future__ import absolute_import, unicode_literals

from celery import shared_task
from stories.models import Story

@shared_task
def add(x, y):
    return x + y

@shared_task
def story_count():
    return Story.objects.count()
