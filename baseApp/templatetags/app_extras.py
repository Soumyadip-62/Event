from django import template
from datetime import date


register = template.Library()

@register.filter(name='current_data')
def current_data(product):

    return date.today().strftime("%m/%d/%Y ")
