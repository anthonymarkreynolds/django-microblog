from django import template
from ..models import Like
from django.utils.timesince import timesince
from django.utils import timezone

register = template.Library()


@register.filter
def custom_timesince(value):
    now = timezone.now()
    # delta = now - value

    # Use timesince to get a string representation of the time delta
    timesince_str = timesince(value, now)

    # Split the string into units
    parts = timesince_str.split(', ')

    # Keep only the first unit
    most_significant_unit = parts[0]

    return most_significant_unit


@register.filter(name='has_liked')
def has_liked(user, post):
    return Like.objects.filter(user=user, post=post).exists()
