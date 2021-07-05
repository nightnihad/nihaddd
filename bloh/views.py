from django.shortcuts import render,HttpResponse
from django.db.models import Model
from bloh.models import *
from customer.models import CustomerModel
# Create your views here.
def index(request):
    istifadeci=CustomerModel.objects.all()
    madel=Addermodel.objects.all()
    context={
        'madel':madel,
        'istifadeci':istifadeci
    }
    return render(request,'index.html',context)
def statistika(request):
    return render(request,'statistika.html')
def create(request):
    return render(request,'create.html')