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
def vista_admin(request):
    return render(request, "restaurant/vista_admin.html")
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

    return render(request,'restaurant/editar.html',datos)