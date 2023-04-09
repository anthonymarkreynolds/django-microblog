from django import template
from ..models import Like

register = template.Library()

@register.filter(name='has_liked')
def has_liked(user, post):
    return Like.objects.filter(user=user, post=post).exists()