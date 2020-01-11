from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import hostel_list

urlpatterns =[   
    path('hostel/',hostel_list), 
    path('hostelform/',hostel_form),
    path('hostelform/save',hostel_save),
    path('hostel/edit/<int:ID>',hostel_edit),
    path('hostel/edit/update/<int:ID>',hostel_update_save),
    path('hostel/delete/<int:ID>',hostel_delete),
    path('search/',search),
    path('hostel/upload/save',upload)
    
    
]
