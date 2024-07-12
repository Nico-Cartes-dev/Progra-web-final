from django.contrib import admin
from .models import Cuenta, Producto, Boleta, ProductoEnBoleta

# Register your models here.

admin.site.register(Cuenta)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(ProductoEnBoleta)