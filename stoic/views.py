from django.shortcuts import render
from django.http import HttpResponse

from .models import Stoic
from .templates import stoic


def index(request):
    stoic = Stoic.objects.all()
    context = {
        'stoic': stoic,
        'title': 'Список Рассуждений'
    }
    return render(request, template_name='stoic/index.html', context=context)


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
