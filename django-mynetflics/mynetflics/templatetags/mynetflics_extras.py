from django import template

register = template.Library()

@register.filter
def joinby(value, arg):
    return arg.join(value)

#@register.filter(name='cut')
#def cut(value, arg):
#    return value.replace(arg, '')

@register.filter
def lower(value):
    return value.lower()

@register.filter
def capitalize(value):
    return value.title()

@register.filter
def space_to_underscore(value):
    return value.replace(" ", "_")

@register.filter
def underscore_to_space(value):
    return value.replace("_", " ")

@register.filter
def to_url_compatible(value):
    return space_to_underscore(lower(value))