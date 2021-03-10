from django.shortcuts import render
from django.http import HttpResponse

from .models import Stoic, Month


def index(request):
    stoic = Stoic.objects.all()
    months = Month.objects.all()
    context = {
        'stoic': stoic,
        'title': 'Список Рассуждений',
    }
    return render(request, template_name='stoic/index.html', context=context)


def get_month(request, month_id):
    stoic = Stoic.objects.filter(month_id=month_id)
    month = Month.objects.get(pk=month_id)
    return render(request, 'stoic/month.html', {'stoic': stoic, 'month': month})