from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

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
    cod_prod= models.IntegerField( primary_key=True, verbose_name='id producto')
    nombre=models.CharField(max_length=25,verbose_name='Nombre Produtcto')
    desc= models.CharField(max_length=144, verbose_name="Descripcion")
    precio= models.IntegerField(verbose_name='precio')
    img=models.ImageField(upload_to = 'restaurant/static/restaurant/img/',verbose_name='Imagen')
    #en linea anterior se ha cambiado la ruta para guardar documentos en la carpeta static en vez de carpeta generada por bdd
    def __str__(self):
        return self.nombre
#fin tipos de producto