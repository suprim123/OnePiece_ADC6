from django.urls import path
from RESTAPI.views import *
from .views import *
urlpatterns=[
    path('ap',hostDetail),
    path('ap/<int:Id>',hostUD),
    path('api/page/<int:PAGENO>/<int:SIZE>',pagination),
]