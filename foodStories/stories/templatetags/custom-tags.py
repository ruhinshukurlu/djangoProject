from django import template
from stories.forms import SubscribeForm

register = template.Library()

@register.simple_tag
def subscribe_form():
    return SubscribeForm