from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from django.urls import reverse_lazy
from .forms import ProductoForm, ClienteForm, BusquedaForm
from .models import Producto, Cliente, Pedido

class IngresarProductoView(FormView):
    template_name = 'ingresar_producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('ingresar_producto')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class IngresarClienteView(FormView):
    template_name = 'ingresar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('ingresar_cliente')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BuscarProductoView(FormView):
    template_name = 'buscar_producto.html'
    form_class = BusquedaForm

    def form_valid(self, form):
        termino_busqueda = form.cleaned_data['termino_busqueda']
        resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
        return render(self.request, 'resultados_busqueda.html', {'resultados': resultados})

class ListaProductosView(View):
    template_name = 'productos.html'

    def get(self, request):
        productos = Producto.objects.all()
        return render(request, self.template_name, {'productos': productos})

class ListaClientesView(View):
    template_name = 'clientes.html'

    def get(self, request):
        clientes = Cliente.objects.all()
        return render(request, self.template_name, {'clientes': clientes})

class ListaPedidosView(View):
    template_name = 'pedidos.html'

    def get(self, request):
        pedidos = Pedido.objects.all()
        return render(request, self.template_name, {'pedidos': pedidos})

