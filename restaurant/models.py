from functools import total_ordering
from pyexpat import model
from tabnanny import verbose
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
import django.contrib.admin
from django.contrib.auth.models import User

# Create your models here.

#Modelo para Comidas

class Comida(models.Model):
    idComida = models.IntegerField(primary_key=True, verbose_name='ID Producto')
    tipoProducto = models.CharField(max_length=20, verbose_name='Tipo de Producto')

    def __str__(self):
        return self.tipoProducto
#Fin Modelo para comidas

#tipos de producto

class Producto(models.Model):
    cod_prod= models.AutoField( primary_key=True, verbose_name='id producto')
    nombre=models.CharField(max_length=25,verbose_name='Nombre Produtcto')
    desc= models.CharField(max_length=144, verbose_name="Descripcion")
    precio= models.IntegerField(verbose_name='precio')
    stock= models.IntegerField(verbose_name='stock', null=True, blank=True)
    img=models.ImageField(upload_to = 'restaurant/static/restaurant/img/',null=True,verbose_name='Imagen',blank=True)
    categoria=models.ForeignKey(Comida,null=True,on_delete=models.CASCADE)
    #en linea anterior se ha cambiado la ruta para guardar documentos en la carpeta static en vez de carpeta generada por bdd
    def __str__(self):
        return self.nombre
#fin tipos de producto

#modelo para usuarios
class Usuarios(models.Model):
    usrN= models.CharField(max_length=30,verbose_name="Nombre de Usuario")
    pswrdN= models.CharField(max_length=15, verbose_name="Contraseña")
    pswrdN2=models.CharField(max_length=15, verbose_name="Contraseña2")
#fin modelos para usuarios

#se crea modelo de token
class Tokens(models.Model):
    token= models.CharField(max_length=256)
    user = models.CharField(max_length=256)

class Customer(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    cliente = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank = True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    pagoProcesado = models.BooleanField(default=False)
    enPreparacion = models.BooleanField(default=False)
    enRetiro = models.BooleanField(default=False)
    retirado = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Producto, on_delete = models.SET_NULL, blank = True,null=True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL,blank = True,null =True)
    quantity = models.IntegerField(default = 0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.precio * self.quantity
        return total
    
