from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def unzip(value,arg):
    return map(str,[a[arg] for a in value])
    
@register.filter
def toint(value):
    return map(float,value)

@register.filter
def col_size(value):
	cols = [6,6,4]
	if value==1:
		return "offset-xs-3 col-xs-"+str(cols[value-1])
	elif value>0 and value <=3:
		return "col-xs-"+str(cols[value-1])
	else:
		return "col-xs-12"


