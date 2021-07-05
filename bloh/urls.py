from django.contrib import admin
from django.urls import path
from django.conf import Settings
from .views import statistika,create,index

urlpatterns=[
    path('',index,name='index'),
    path('create/',create,name='create'),
    path('statictics/',statistika,name='statistika')
]