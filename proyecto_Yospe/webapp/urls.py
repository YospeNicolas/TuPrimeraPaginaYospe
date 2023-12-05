from django.urls import path
from .views import ingresar_producto

urlpatterns = [
    path('ingresar-producto/', ingresar_producto, name='ingresar_producto'),

    path('', ingresar_producto, name='raiz'), 
]
