from turtle import delay
from django.shortcuts import redirect, render
from restaurant.forms import ProductoForm  #creaUsuario
from restaurant.models import Producto
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views hera
def menu(request):
    listaProductos = Producto.objects.all()
    datos ={
        'productos':listaProductos
    }
    return render(request, "restaurant/menu.html",datos)
def index(request):
    return render(request,"restaurant/index.html")

def login(request): #implementar cifrado sha256
    ##username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(request,username=username,password=password)
    #if user is not None:
        #login(request,user)
        #return redirect(vista_admin)
    #else:
    return render(request,"restaurant/login.html")
def recuperar(request):
    return render(request,"restaurant/recuperar.html")
def newUser(request):
    form = creaUsuario(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('usuario')
        password = form.cleaned_dataa.get('password1')
        user = authenticate(username=username, password=password)
        login(request,user)
    return render(request,"restaurant/newUser.html",{'form':form})
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

def form_del_producto(request,id):
    producto=Producto.objects.get(cod_prod=id)
    producto.delete()
    return redirect(to='vista_admin')

