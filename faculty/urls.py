# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty, name='/'),
    path('info', views.employee_info, name='info'),
    
]