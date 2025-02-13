from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

class Carrito(models.Model):
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Relación con usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) # Relación con producto
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad
    