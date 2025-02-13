from django.urls import path
from .views import ver_carrito, agregar_producto, eliminar_producto, finalizar_compra

urlpatterns = [
    path('', ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>', agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
    path('finalizar/', finalizar_compra, name='finalizar_compra'),
]