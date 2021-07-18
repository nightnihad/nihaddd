from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from .models import CustomerModel
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .forms import  LoginForm,RegisterForm
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
# Create your views here.
def user(request):
    return render(request,'profil.html')
@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form=RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password1= form.cleaned_data.get("password1")
            newUser =CustomerModel(username =username)
            newUser.set_password(password1)
            newUser.save()
            auth_login(request,newUser)
            messages.success(request,"XOŞ GƏLMİSİNİZ ")
            return redirect('/')
        messages.success(request,'Qeyd olunmadınız')
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})
@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
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
        messages.success(request,'Qeyd olundunuz')
        return redirect('/')
    return render(request,'login.html',context)
def logout(request):
    auth_logout(request)
    messages.success(request,'Çıxış etdiniz',)
    return redirect('/')
def profil(request,id):

    return render(request,'profil.html')

