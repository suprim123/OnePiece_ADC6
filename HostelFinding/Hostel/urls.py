from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import hostel_list

app_name = "Hostel"
urlpatterns =[ 
    path('',home,name="Home"), 
    path('hostellogin/', hostel_login),
    path('home/',home,name="Home"),  
    path('hostellist/',hostel_list, name="list"), 
    path('hostelform/',Hostel_form),
    path('hostellist/edit/<int:ID>',hostel_edit, name="edit"),
    path('hostellist/edit/update/<int:ID>',hostel_update_save),
    path('hostellist/delete/<int:ID>',hostel_delete,name="delete"),
    path('search/',search),
    path('hostellist/upload/save',upload),
    path('signup/',view_register_user),
    path('login/',view_authenticate_user),
    path('logout/',logout,name = "logout")
  
    
    
   

    
    
    
]
