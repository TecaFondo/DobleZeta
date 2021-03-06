#from cgitb import html
#from tkinter import Menu
from unicodedata import name
from django.urls import path,include
from restaurant.views import * 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


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
    path('logout/',cerrarsesion, name='cerrarsesion'), #tanto este logout como el logout de la linea 26 cumplen la misma funcion, este es desde views, el otro es desde google
    #path('googleLogin', googleLogin,name='googleLogin'),  #esto lleva al inicio de sesion de google (Se encuentra comentado pq ya no es necesario)
    path('accounts/', include('allauth.urls')), #se importa para el uso de google
    path('logout', LogoutView.as_view()),
    path('nuevoProdApi/',nuevoProdApi,name='nuevoProdApi'),
    path('editProdApi/<id>',editProdApi,name='editProdApi'),
    path('delProdApi/<id>',delProdApi,name='delProdApi'),
    path('update_item/', updateItem, name="update_item"),
    path('carrito/',carrito,name='carrito'),
    path('procesar/',procesar_compra,name='procesar_compra'),
    path('tienda/',store,name='store'),
    path('seguimiento/',seguimiento, name='seguimiento'),
    path('pedidos/',pedidos,name='pedidos'),
    path('cambioestado/',cambioestado,name='cambioestado'),
    path('cambio/<id>',cambio,name='cambio'),
    #path('form-productos',form_productos,name='form_productos'),   
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)