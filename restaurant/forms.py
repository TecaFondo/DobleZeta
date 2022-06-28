from dataclasses import fields
from pyexpat import model
from tabnanny import verbose
from django import forms
from django.forms import ModelForm
from restaurant.models import Producto, Usuarios
from allauth.account.forms import LoginForm

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['cod_prod','nombre', 'desc', 'precio','img','categoria']

class UsuariosForm(ModelForm):
    #se da formato a cada uno de los campos dentro de la forma
    usrN = forms.CharField(widget=forms.EmailInput(attrs={'class':'login-username','placeholder':'Email'}),label='')
    pswrdN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')
    pswrdN2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Repetir Contraseña'}),label='')
    class Meta:
        #se asigna modelo y orden de aparicion en html
        model = Usuarios
        fields= ['usrN','pswrdN','pswrdN2']

class LoginForm(ModelForm):
    usrN = forms.CharField(widget=forms.TextInput(attrs={'class':'login-username','placeholder':'Username'}),label='')
    pswrdN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')
    class Meta:
        model=Usuarios
        fields= ['usrN','pswrdN']

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['usrN'] = forms.CharField(widget=forms.TextInput(attrs={'class':'login-username','placeholder':'Username'}),label='')
        self.fields['pswrdN'] = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')