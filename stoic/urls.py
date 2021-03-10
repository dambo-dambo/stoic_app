from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('month/<int:month_id>/', get_month, name='month'),
]