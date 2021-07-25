from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.db.models import Model
from bloh.models import *
from customer.models import CustomerModel
from .forms import Accountsetting, Commentform, Creat, Upgrade
from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    istifadeci=CustomerModel.objects.all()
    madel=Addermodel.objects.all()
    erazi=AreaCategorymodel.objects.all()
    if request.method =='GET':
        if request.user.is_authenticated:
            context={
            'madel':madel,
            'istifadeci':istifadeci,
            'erazi' :erazi
            }
            return render(request,'index.html',context)
        messages.success(request,'İlk öncə qeydiyyatdan keçin')
        return redirect('customer:login')
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
            messages.success(request,'Yazı Yaradıldı')
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
                messages.success(request,'dəyişikliklər edildi')
                return redirect('index')
    mal={
    'form':form
    }

    return render(request,'update.html',mal)
@login_required(login_url='/')
def delete(request,id):
    Entry=Addermodel.objects.filter(id=id)
    if request.method =='POST':
        Entry.delete()
        messages.success(request,'Başarıyla silindi')
        return redirect('index')
    context={
        'Entry': Entry
    }
    return render(request,'delete.html',context)
@login_required(login_url='/')
def dashboard(request):
    customer=request.user
    Entri=Addermodel.objects.filter(author=customer)
    context={
        'Entri':Entri,
        'customer':customer
    }
    return render(request,'dashboard.html',context)
@login_required(login_url='/')
def account_settings(request):
    users=request.user
    form=Accountsetting(instance=users)
    if request.method=='POST':
        form=Accountsetting(request.POST,request.FILES,instance=users)
        if form.is_valid():
            form.save()
            messages.success(request,'profil dəyişikliyi edildi')
            return redirect('customer:profil')
    can={
        'form':form
    }

    return render(request,'account_settings.html',can)
@login_required(login_url='/')
def commentcreate(request):
    form1=Commentform()
    if request.method=='POST':
        form1=Commentform(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('customer:profil')
    conten={
            'form1':form1
        }
    return render(request,'commentcreate.html',conten)
def updatec(request,id):
    comm=Commentarticle.objects.get(id=id)
    formm=Commentform(instance=comm)
    if request.method =='POST':
        formm=Commentform(request.POST,instance=comm)
        if formm.is_valid():
            formm.save()
            return redirect('customer:profil')
    terkibb={
    'formm':formm
    }
    return render(request,'updatec.html',terkibb)
def deletec(request,id):
    comment=Commentarticle.objects.filter(id=id)
    if request.method=='POST':
        comment.delete()
        return redirect('customer:profil')
    terkib={
            'comment':comment
        }
    return render(request,'deletec.html',terkib)