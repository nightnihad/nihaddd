from django.contrib import admin
from django.urls import path
from django.conf import settings
from customer.views import *

urlpatterns=[
    path('user/',user,name='user'),
    path('register/',register,name='register')
]