from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from RegisterAndLogin.forms import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', include('caosnoticias.urls')),
    path('sesion/', include('RegisterAndLogin.urls')),
    path('subir_noticias/', include('subir_noticias.urls')),
    path('suscripciones/', include('suscripciones.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)