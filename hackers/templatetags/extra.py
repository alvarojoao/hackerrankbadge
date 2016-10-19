from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def unzip(value,arg):
    return map(str,[a[arg] for a in value])
    

@register.filter
def toint(value):
    return map(int,value)


