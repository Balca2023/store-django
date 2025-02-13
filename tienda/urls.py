from django.contrib import admin
from django.urls import path, include
from .views import registro
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),
    path('registro/', registro, name='registro'),  # Nueva ruta para el registro
    path('login/', LoginView.as_view(template_name='login.html', next_page='/productos/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('productos/', include('productos.urls')),
    path('carrito/', include('carrito.urls')),
]

# Habilitar el acceso a archivos multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])