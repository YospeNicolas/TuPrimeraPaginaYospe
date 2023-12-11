from django.urls import path
from .views import (
    IngresarProductoView,
    IngresarClienteView,
    BuscarProductoView,
    ListaProductosView,
    ListaClientesView,
    ListaPedidosView
)

urlpatterns = [
    path('ingresar-producto/', IngresarProductoView.as_view(), name='ingresar_producto'),
    path('ingresar-cliente/', IngresarClienteView.as_view(), name='ingresar_cliente'),
    path('buscar-producto/', BuscarProductoView.as_view(), name='buscar_producto'),
    path('lista-productos/', ListaProductosView.as_view(), name='lista_productos'),
    path('lista-clientes/', ListaClientesView.as_view(), name='lista_clientes'),
    path('lista-pedidos/', ListaPedidosView.as_view(), name='lista_pedidos'),
]

