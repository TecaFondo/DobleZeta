from django.urls import path
from rest_comidas.views import list_productos, detalle_productos

urlpatterns=[
    path('list_productos',list_productos,name='list_productos'),
    path('detalle_productos/<id>',detalle_productos,name='detalle_productos'),
]