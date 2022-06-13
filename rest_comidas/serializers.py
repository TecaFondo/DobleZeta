from tkinter import Image
from rest_framework import serializers
from restaurant.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['cod_prod','nombre', 'desc', 'precio','img','categoria']
    
class ImageSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=True)
    class Meta:
        model = Producto
        fields = ['cod_prod','nombre', 'desc', 'precio','img','categoria']