from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import hostel_list

urlpatterns =[   
    path('hostel/',hostel_list), 
    path('hostelform/',hostel_form),
    path('hostelform/save',hostel_save),
    
   
]
