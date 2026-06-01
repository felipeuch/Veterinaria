from django import forms
from django.forms import ModelForm
from .models import Mascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class MascotaForm(ModelForm):
    
    nombre = forms.CharField(min_length=3, max_length=80)
    descripcion = forms.CharField(min_length=3, max_length=200) 
    color = forms.CharField(min_length=3, max_length=20)
    peso = forms.CharField(min_length=1)
    fecha_nacimiento_mascota = forms.DateField()

    
    class Meta:
        model = Mascota
        fields = ['nombre','descripcion','color','peso','fecha_nacimiento_mascota','imagen']


 
         
    