#from cgitb import html
#from tkinter import Menu
from django.urls import path
from .views import menu, index, login, newUser, recuperar

urlpatterns =[
    path('',index, name='index'),
    path('index/',index, name='index'),
    path('menu/', menu, name='menu'),
    path('login/', login, name='login'),
    path('newUser/', newUser, name='newUser'),
    path('recuperar/', recuperar, name='recuperar'), 
    #path('form-productos',form_productos,name='form_productos'),   
]