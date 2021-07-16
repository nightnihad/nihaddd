from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from .models import CustomerModel
from django.contrib.auth.forms import UserCreationForm
from .forms import  LoginForm
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
# Create your views here.
def user(request):
    return render(request,'profil.html')
def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'register.html',{'form':form})
def login(request):
    form=LoginForm(request.POST or None)
    context={
            'form':form
        }
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user1=authenticate(username=username,password=password)
        if user1 is None:
            return render(request,'login.html',context)
        auth_login(request,user1)
        return redirect('/')
    return render(request,'login.html',context)
def logout(request):
    auth_logout(request)
    return redirect('/')

