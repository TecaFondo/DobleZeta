from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from restaurant.models import Producto
from rest_comidas.serializers import ProductoSerializer


#Se crea la api
@csrf_exempt
@api_view(['GET','POST'])
def list_productos(request):
    if request.method =='GET':
        listProductos = Producto.objects.all()
        serializer= ProductoSerializer(listProductos, many =True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = ProductoSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def detalle_productos(request,id):
    try:
        producto =Producto.objects.get(cod_prod = id)
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data = dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)