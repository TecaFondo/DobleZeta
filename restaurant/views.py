from django.shortcuts import render

# Create your views hera
def menu(request):
    return render(request, "restaurant/menu.html")
def index(request):
    return render(request,"restaurant/index.html")
def login(request):
    return render(request,"restaurant/login.html")
def recuperar(request):
    return render(request,"restaurant/recuperar.html")
def newUser(request):
    return render(request,"restaurant/newUser.html")
