from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Carrito
from productos.models import Producto

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)  # Filtrar por usuario
    total = sum(item.subtotal() for item in carrito)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito, 'total': total})

@login_required
def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)  
    item, created = Carrito.objects.get_or_create(producto=producto, usuario=request.user)  # Asociar con usuario

    if not created:
        item.cantidad += 1
        item.save()

    return redirect('ver_carrito')

@login_required
def eliminar_producto(request, producto_id):
    item = get_object_or_404(Carrito, producto__id=producto_id, usuario=request.user)  # Filtrar por usuario

    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()

    return redirect('ver_carrito')

@login_required
def finalizar_compra(request):
    Carrito.objects.filter(usuario=request.user).delete()  # Asegurar que solo elimine el carrito del usuario
    return redirect('ver_carrito')
