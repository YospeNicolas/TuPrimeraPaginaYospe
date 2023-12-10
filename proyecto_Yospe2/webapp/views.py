from django.shortcuts import render, redirect
from .forms import ProductoForm, ClienteForm, BusquedaForm
from .models import Producto

def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingresar_producto')  # Puedes cambiar 'ingresar_producto' por el nombre de la vista
    else:
        form = ProductoForm()

    return render(request, 'ingresar_producto.html', {'form': form})

def ingresar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingresar_cliente')
    else:
        form = ClienteForm()

    return render(request, 'ingresar_cliente.html', {'form': form})

def buscar_producto(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()

    return render(request, 'buscar_producto.html', {'form': form})
