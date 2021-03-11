from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, CreateView


from .forms import StoicForm, UserRegisterForm, UserLoginForm, ContactForm
from .models import Stoic, Month
from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'stoic/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'stoic/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'loc@aaa.net', ['978@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'stoic/test.html', {"form": form})


class HomeStoic(MyMixin, ListView):

    model = Stoic
    template_name = 'stoic/home_stoic_list.html'
    context_object_name = 'stoic'
    mixin_prop = 'hello world'
    # extra_context = {'title': 'Главная'}
    paginate_by = 2



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Стоик')
        context['mixin_prop'] = self.get_prop()
        return context
#фильтруем запрос для отображения

    def get_queryset(self):
        return Stoic.objects.filter(is_published=True).select_related('month')


class StoicByMonth(MyMixin, ListView):
    model = Stoic
    template_name = 'stoic/home_stoic_list.html'
    context_object_name = 'stoic'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Month.objects.get(pk=self.kwargs['month_id']))
        return context

    def get_queryset(self):
        return Stoic.objects.filter(month_id=self.kwargs['month_id'], is_published=True).select_related('month')


class ViewStoic(DetailView):
    model = Stoic
    context_object_name = 'stoic_item'
    # template_name = 'stoic/stoic_detail.html'
    # pk_url_kwarg = 'stoic_id'


class CreateStoic(LoginRequiredMixin, CreateView):
    form_class = StoicForm
    template_name = 'stoic/add_stoic.html'
    #success_url = reverse_lazy('home')
    login_url = '/admin/'
    #raise_exception = True


# def index(request):
#     stoic = Stoic.objects.all()
#     months = Month.objects.all()
#     context = {
#         'stoic': stoic,
#         'title': 'Список Рассуждений',
#     }
#     return render(request, template_name='stoic/index.html', context=context)


# def get_month(request, month_id):
#     stoic = Stoic.objects.filter(month_id=month_id)
#     month = Month.objects.get(pk=month_id)
#     return render(request, 'stoic/month.html', {'stoic': stoic, 'month': month})


# def view_stoic(request, stoic_id):
#     stoic_item = get_object_or_404(Stoic, pk=stoic_id)
#     return render(request, 'stoic/view_stoic.html', {"stoic_item": stoic_item})
#
#
# def add_stoic(request):
#     if request.method == 'POST':
#         form = StoicForm(request.POST)
#         if form.is_valid():
#
#             stoic = form.save()
#             return redirect(stoic)
#     else:
#         form = StoicForm()
#     return render(request, 'stoic/add_stoic.html', {'form': form})

