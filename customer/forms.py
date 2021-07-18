from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import CustomerModel
class LoginForm(forms.Form):
    username= forms.CharField(label='username', 
                    widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password= forms.CharField(label='parol', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomerModel
        fields=['username','email','password1','password2']
        widgets = {
        'username': forms.fields.TextInput(attrs={'placeholder': 'username'}),

        'email': forms.fields.TextInput(attrs={'placeholder': 'email stuff'})
        }