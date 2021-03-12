from django.urls import path, include

from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    path('', HomeStoic.as_view(), name='home'),
    # path('month/<int:month_id>/', get_month, name='month'),
    path('month/<int:month_id>/', StoicByMonth.as_view(), name='month'),
    # path('stoic/<int:stoic_id>/', view_stoic, name='view_stoic'),
    path('stoic/<int:pk>/', ViewStoic.as_view(), name='view_stoic'),
    # path('stoic/add-stoic/', add_stoic, name='add_stoic'),
    path('stoic/add-stoic/',  CreateStoic.as_view(), name='add_stoic'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
