from __future__ import absolute_import, unicode_literals

from celery import shared_task
from stories.models import Story, Subscribe
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@shared_task
def add(x, y):
    return x + y

@shared_task
def story_count():
    return Story.objects.count()

@shared_task
def nootify_subscriber():
    subject = 'Hello, new stories from FoodStories'
    subscribers = list(Subscribe.objects.values_list('email', flat = True))
    stories = Story.objects.all()
    context = {
        'stories' : stories
    }
    html_content = render_to_string('email-subscribers.html', context)
    msg = EmailMultiAlternatives(subject=subject, to = subscribers)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
