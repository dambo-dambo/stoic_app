from django.urls import path

from .views import *


urlpatterns = [
    path('', HomeStoic.as_view(), name='home'),
    path('month/<int:month_id>/', get_month, name='month'),
    path('stoic/<int:stoic_id>/', view_stoic, name='view_stoic'),
    path('stoic/add-stoic/', add_stoic, name='add_stoic'),
]