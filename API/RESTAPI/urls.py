from django.urls import path
from RESTAPI.views import *
urlpatterns=[
    path('ap',hostDetail),
    path('ap/<int:Id>',hostUD)
]