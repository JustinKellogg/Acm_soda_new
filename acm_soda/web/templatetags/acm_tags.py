from django import template

register = template.Library()

@register.filter('dollars')
def dollars(value):
    return "%.2f" % (value/100.0)