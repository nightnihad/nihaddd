from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import Settings
from .views import account_settings, dashboard, statistika,create,index,delete,update
app_name='blog'
urlpatterns=[
    path('index',index,name='index'),
    path('create/',create,name='create'),
    path('statictics/',statistika,name='statistika'),
    path('delete/<str:id>',delete,name='delete'),
    path('update/<str:id>',update,name='update'),
    path('dashboard',dashboard,name='dashboard'),
    path('account_settings/',account_settings,name='account_settings'),
]