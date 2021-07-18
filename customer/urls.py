from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from django.conf import settings
from customer.views import logout, profil, register,login,user

app_name='customer'

urlpatterns=[
    path('user/',user,name='user'),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('profil/<str:id>',profil,name='profil')
]