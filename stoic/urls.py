from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('month/<int:month_id>/', get_month),
]
