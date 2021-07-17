from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import CustomerModel
class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomerModel
        fields=['username','email','password1','password2']