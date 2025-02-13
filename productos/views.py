from django.shortcuts import render
from django.conf import settings  # Importar settings para acceder a MEDIA_URL
from .models import Producto  # Importación correcta del modelo

def catalogo(request):
    productos = Producto.objects.filter(disponible=True)  # Filtra productos disponibles
    return render(request, 'productos/catalogo.html', {
        'productos': productos,
        'MEDIA_URL': settings.MEDIA_URL,  # Pasar MEDIA_URL al template
    })
