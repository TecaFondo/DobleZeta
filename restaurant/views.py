from django.shortcuts import render
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
