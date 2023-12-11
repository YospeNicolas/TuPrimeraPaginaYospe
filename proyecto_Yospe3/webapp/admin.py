from django.contrib import admin
from .models import Producto, Cliente, Pedido, Factura

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cliente', 'cantidad')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'total')

