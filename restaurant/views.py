from email import header
from telnetlib import LOGOUT
from tokenize import group
from turtle import delay
from django.shortcuts import redirect, render
from restaurant.forms import ProductoForm,UsuariosForm,LoginForm
from restaurant.models import Producto, Usuarios
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User, Group
from django.http import HttpRequest, HttpResponseRedirect
from rest_framework.authentication import TokenAuthentication
from rest_comidas.viewsLogin import login as api_login
#se importan clases de api
import json
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response as apiResponse
from rest_framework.views import APIView
import requests
# Create your views hera

def is_staff(user):
    return user.is_authenticated and user.Cliente

@login_required
def menu(request):
    listaProductos = Producto.objects.all()
    datos ={
        'productos':listaProductos
    }
    return render(request, "restaurant/menu.html",datos)
@login_required
def index(request):
    return render(request,"restaurant/index.html")

def user_login(request):
    datos={
        'form':LoginForm()
    }
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            usernameU = request.POST['usrN']
            passwordU = request.POST['pswrdN']
            user = authenticate(username=usernameU,password=passwordU)
            if user is not None:
                login(request,user)
                return render(request, "restaurant/recuperar.html")
    return render(request,"restaurant/login.html",datos)
#recuperar contraseña
def recuperar(request):
    return render(request,"restaurant/recuperar.html")

#se crea usuario nuevo y token
def newUser(request): 
    datos={
        'form':UsuariosForm()
    }
    if(request.method == 'POST'):
        form=UsuariosForm(request.POST)
        if form.is_valid():
            #obtiene los datos del usuario desde formulario
            usernameN = form.cleaned_data.get('usrN')
            passwordN = form.cleaned_data.get('pswrdN')
            passwordN2= form.cleaned_data.get('pswrdN2')
            try:
                #se verifica existencia del usuario
                user = User.objects.get(username = usernameN)
            except User.DoesNotExist:
                #si no existe se genera un nuevo usuario validando si es que las pswrd son identicas
                if(passwordN == passwordN2):
                    user = User.objects.create_user(username=usernameN,email=usernameN,password=passwordN)
                    user = authenticate(username=usernameN, password=passwordN) #autentifican las credenciales del usuario
                    #se asigna un grupo al usuario nuevo (default comprador)
                    my_group = Group.objects.get(name='Comprador')
                    user.groups.add(my_group)
                    #se logea al usuario nuevo
                    login(request,user)
                    #comienzo de creacion de token
                    body= {"username": usernameN ,"password" : passwordN} #se genera json con info de usuario creado
                    r = requests.post('http://localhost:8000/api/login',data=json.dumps(body)) # se realiza la creacion de token
                    print(r.text) #se imprime token en forma  de debug
                    #fin creacion token
                    return render(request, "restaurant/index.html")
    return render(request,"restaurant/newUser.html",datos)


@user_passes_test(is_staff)
def vista_admin(request):
    productos = Producto.objects.all()
    datos ={
        'productos':productos
    }

    return render(request, "restaurant/vista_admin.html",datos)
    
def carga(request):
    datos={
        'form':ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST or None, request.FILES or None) #se agrega request file para cargar imágenes
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Guardados correctamente'
        else:
            datos['mensaje']='no se ha guardado uwu'
    return render(request,'restaurant/carga.html',datos)
@login_required
def form_mod_producto(request,id):
    producto=Producto.objects.get(cod_prod=id)
    datos={
        'form':ProductoForm(instance=producto)
    }

    if(request.method == 'POST'):
        formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Modificados correctamente'
            return redirect(vista_admin)
        datos['mensaje']='NO se ha podido modificar datos'
    return render(request,'restaurant/editar.html',datos)
@login_required
def form_del_producto(request,id):
    producto=Producto.objects.get(cod_prod=id)
    producto.delete()
    return redirect(to='vista_admin')

def cerrarsesion(request):
    logout(request)
    return redirect(user_login)

#def googleLogin(request): #Se envia a usuario a pagina login de google (Se comenta ya que ahora no se utiliza)
#    return render(request, 'restaurant/googleLogin.html')
