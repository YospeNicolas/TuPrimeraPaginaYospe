# proyecto_Yospe/urls.py
from django.contrib import admin
from django.urls import path, include  # Asegúrate de incluir 'include'
from webapp.views import ListaProductosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaProductosView.as_view(), name='lista_productos'),  # Redirige la URL raíz a la lista de productos
    path('ingresar-producto/', include('webapp.urls')),  # Incluye las URLs de tu aplicación webapp
]


