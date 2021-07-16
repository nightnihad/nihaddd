from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import Settings
from .views import dashboard, statistika,create,index,delete,upgrade
app_name='blog'
urlpatterns=[
    path('index',index,name='index'),
    path('create/<str:id>',create,name='create'),
    path('statictics/',statistika,name='statistika'),
    path('delete/<str:id>',delete,name='delete'),
    path('upgrade/<str:id>',upgrade,name='upgrade'),
    path('dashboard/<str:id>',dashboard,name='dashboard'),
]