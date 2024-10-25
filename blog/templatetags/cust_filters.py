from django import template
register = template.Library()

@register.filter(name='f100')
def first_100char(value):
    result = value[:100]
    return result