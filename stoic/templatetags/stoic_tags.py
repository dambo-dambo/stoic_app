from django import template

from stoic.models import Month

register = template.Library()


@register.simple_tag(name='get_list_months')
def get_months():
    return Month.objects.all()


@register.inclusion_tag('stoic/list_months.html')
def show_months(arg1='Hello', arg2='world'):
    months = Month.objects.all()
    return {"months": months, "arg1": arg1, "arg2": arg2}
