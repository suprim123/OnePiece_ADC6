from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import hostel_list

appname = "Hostel"
urlpatterns =[   
    path('hostel/',hostel_list), 
    path('hostelform/',Hostel_form),
    path('hostelform/save',hostel_save),
    path('hostel/edit/<int:ID>',hostel_edit),
    path('hostel/edit/update/<int:ID>',hostel_update_save),
    path('hostel/delete/<int:ID>',hostel_delete),
    path('search/',search),
    path('hostel/upload/save',upload),
    path('signup/',view_register_user),
    path('login/',view_authenticate_user),
    path('logout/',logout,name = "logout"),
    path('home/',home,name="Home"),
    path('upload/',upload),
    # path('download/',download),
    
    
   

    
    
    
]
