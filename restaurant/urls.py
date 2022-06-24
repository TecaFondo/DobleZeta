#from cgitb import html
#from tkinter import Menu
from unicodedata import name
from django.urls import path
from restaurant.views import cerrarsesion, menu, index, user_login, newUser, recuperar,carga, form_mod_producto,vista_admin,form_del_producto
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('',user_login, name='index'),
    path('index/',index, name='index'),
    path('menu/', menu, name='menu'),
    path('login/', user_login, name='login'),
    path('newUser/', newUser, name='newUser'),
    path('recuperar/', recuperar, name='recuperar'), 
    path('carga/',carga, name='carga'),
    path('editar/<id>',form_mod_producto,name='form_mod_producto'),
    path('vista_admin/',vista_admin,name='vista_admin'),
    path('borrar-prod/<id>',form_del_producto,name='form_del_producto'),
    path('logout/',cerrarsesion,'cerrarsesion')
    #path('form-productos',form_productos,name='form_productos'),   
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)