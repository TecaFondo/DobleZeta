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
    img=models.CharField(max_length=50,verbose_name='Ruta a imagen')
    
    def __int__(self):
        return self.cod_prod
#fin tipos de producto