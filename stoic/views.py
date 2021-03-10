from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import StoicForm
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


def view_stoic(request, stoic_id):
    stoic_item = get_object_or_404(Stoic, pk=stoic_id)
    return render(request, 'stoic/view_stoic.html', {"stoic_item": stoic_item})


def add_stoic(request):
    if request.method == 'POST':
        form = StoicForm(request.POST)
        if form.is_valid():

            stoic = form.save()
            return redirect(stoic)
    else:
        form = StoicForm()
    return render(request, 'stoic/add_stoic.html', {'form': form})

