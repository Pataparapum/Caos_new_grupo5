
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', include('caosnoticias.urls')),
    path('sesion/', include('RegisterAndLogin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye esta línea
]
