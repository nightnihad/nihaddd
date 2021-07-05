from django.shortcuts import render,HttpResponse

# Create your views here.
def user(request):
    return render(request,'profil.html')
def register(request):
    return render(request,'register.html')