from customer.models import CustomerModel
from django import forms
from django.db.models import fields
from django.forms import Form
from .models import Addermodel
class Upgrade(forms.ModelForm):
    class Meta:
        model=Addermodel
        fields='__all__'

class Creat(forms.ModelForm):
    class Meta:
        model=Addermodel
        fields=['name','area','photo','content']
class Accountsetting(forms.ModelForm):
    class Meta:
        model=CustomerModel
        fields=['username','email','avatar']
        widgets = {
        'username': forms.fields.TextInput(attrs={'placeholder': 'username'}),

        'email': forms.fields.TextInput(attrs={'placeholder': 'email stuff'})
        }