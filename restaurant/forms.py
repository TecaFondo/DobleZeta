from dataclasses import fields
from django import forms
from django.forms import ModelForm
from restaurant.models import Producto, Usuarios

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['cod_prod','nombre', 'desc', 'precio','img','categoria']

class UsuariosForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuarios
        fields= ['usrN']