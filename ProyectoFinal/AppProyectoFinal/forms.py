from email import charset
from django.forms import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from ckeditor.fields import RichTextField

class UserRegisterForm(UserCreationForm):
    
    email = EmailField(help_text=False)
    password1 = CharField(label= "Contraseña", widget=PasswordInput, help_text=False)
    password2 = CharField(label= "Confirmar contraseña", widget=PasswordInput, help_text=False) 
    
    class meta:
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = {k:'' for k in fields}

class UserEditForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}