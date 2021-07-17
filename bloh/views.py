from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.db.models import Model
from bloh.models import *
from customer.models import CustomerModel
from .forms import Creat, Upgrade
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    istifadeci=CustomerModel.objects.all()
    madel=Addermodel.objects.all()
    erazi=AreaCategorymodel.objects.all()
    context={
        'madel':madel,
        'istifadeci':istifadeci,
        'erazi' :erazi
    }
    return render(request,'index.html',context)
def statistika(request):
    return render(request,'statistika.html')
@login_required(login_url='/')
def create(request):
    form=Creat()
    if request.method =='POST':
        form=Creat(request.POST,request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.author=request.user
            article.save()
            return redirect('/')
    context={
        'form':form
    }
    return render(request,'create.html',context)

@login_required(login_url='/')
def update(request,id):
    obyekt=Addermodel.objects.get(id=id)
    form=Upgrade(instance=obyekt)
    if request.method=='POST':
            form=Upgrade(request.POST,request.FILES,instance=obyekt)
            if form.is_valid():
                form.save()
                return redirect('index')
            mal={
                'form':form
            }

            return render(request,'update.html',mal)
def delete(request,id):
    Entry=Addermodel.objects.filter(id=id)
    if request.method =='POST':
        Entry.delete()
        return redirect('index')
    context={
        'Entry': Entry
    }
    return render(request,'delete.html',context)
def dashboard(request,id):
    customer=CustomerModel.objects.get(id=id)
    Entri=Addermodel.objects.filter(author=customer)
    context={
        'Entri':Entri,
        'customer':customer
    }
    return render(request,'dashboard.html',context)

