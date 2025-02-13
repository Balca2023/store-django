import os
from django.db import models
from django.core.files.storage import default_storage

class Categoria(models.Model):
    nombre = models.CharField(max_length=101)

    def __str__(self):
        return self.nombre

def product_image_path(instance, filename):
    """Guardar imágenes con el mismo nombre sin sufijos aleatorios."""
    nombre, extension = os.path.splitext(filename)
    filepath = f"productos/{nombre}{extension}"

    # Construir la ruta completa del archivo en la carpeta media
    full_path = os.path.join('media', filepath)

    # Verificar si ya existe una imagen previa en el mismo campo
    if instance.pk:
        try:
            old_instance = Producto.objects.get(pk=instance.pk)
            if old_instance.imagen and old_instance.imagen.name != filepath:
                old_image_path = os.path.join('media', old_instance.imagen.name)
                if default_storage.exists(old_image_path):
                    default_storage.delete(old_image_path)
        except Producto.DoesNotExist:
            pass  # Si no existe, simplemente lo ignoramos

    return filepath

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    producto = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to=product_image_path, default='productos/no_image.png', blank=True, null=True)

    def __str__(self):
        return self.nombre

