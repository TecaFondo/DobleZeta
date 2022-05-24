from django.urls import path
from rest_comidas.views import list_productos

urlpatterns=[
    path('list_productos',list_productos,name='list_productos'),
]