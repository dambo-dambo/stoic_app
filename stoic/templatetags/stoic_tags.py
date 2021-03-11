from django import template
from django.db.models import Count, F

from stoic.models import Month

register = template.Library()


@register.simple_tag(name='get_list_months')
def get_months():
    return Month.objects.all()


@register.inclusion_tag('stoic/list_months.html')
def show_months(arg1='Hello', arg2='world'):
    #months = Month.objects.all()
    #считает не все, а только опубликованные
    months = Month.objects.annotate(cnt=Count('stoic', filter=F('stoic__is_published'))).filter(cnt__gt=0)
    return {"months": months, "arg1": arg1, "arg2": arg2}
