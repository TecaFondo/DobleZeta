#from cgitb import html
#from tkinter import Menu
from django.urls import path
from .views import menu, index, login, newUser, recuperar,carga, form_mod_producto,vista_admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('',index, name='index'),
    path('index/',index, name='index'),
    path('menu/', menu, name='menu'),
    path('login/', login, name='login'),
    path('newUser/', newUser, name='newUser'),
    path('recuperar/', recuperar, name='recuperar'), 
    path('carga/',carga, name='carga'),
    path('editar/<id>',form_mod_producto,name='form_mod_producto'),
    path('vista_admin/',vista_admin,name='vista_admin')
    #path('form-productos',form_productos,name='form_productos'),   
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)