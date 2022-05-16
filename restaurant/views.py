from django.shortcuts import render
from .forms import ProductoForm
from restaurant.forms import ProductoForm
from .models import Producto
# Create your views hera
def menu(request):
    productos = Producto.objects.all()
    datos ={
        'productos':productos
    }
    return render(request, "restaurant/menu.html",datos)
def index(request):
    return render(request,"restaurant/index.html")
def login(request):
    return render(request,"restaurant/login.html")
def recuperar(request):
    return render(request,"restaurant/recuperar.html")
def newUser(request):
    return render(request,"restaurant/newUser.html")

def carga(request):
    datos={
        'form':ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Guardados correctamente'
        else:
            datos['mensaje']='no se ha guardado uwu'
    return render(request,'restaurant/carga.html',datos)