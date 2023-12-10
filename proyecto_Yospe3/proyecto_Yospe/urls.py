from django.contrib import admin
from django.urls import path, include
from webapp.views import ListaProductosView  # Asegúrate de tener la importación correcta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaProductosView.as_view(), name='lista_productos'),  # Redirige la URL raíz a la lista de productos
    path('ingresar-producto/', include('webapp.urls')),  # Incluye las URLs de tu aplicación webapp
]
