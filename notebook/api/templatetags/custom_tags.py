from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

@register.filter(name='trim')
@stringfilter
def trim(value):
    return value.strip()