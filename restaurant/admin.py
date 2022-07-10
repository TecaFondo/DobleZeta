from django.contrib import admin
from restaurant.models import  *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Comida)
admin.site.register(Producto)
admin.site.register(Order)
admin.site.register(OrderItem)