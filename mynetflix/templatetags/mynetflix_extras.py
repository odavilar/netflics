from django import template

register = template.Library()

@register.filter
def joinby(value, arg):
    return arg.join(value)

#@register.filter(name='cut')
#def cut(value, arg):
#    return value.replace(arg, '')

#@register.filter
#def lower(value):
#    return value.lower()

#register.filter('joinby', joinby)