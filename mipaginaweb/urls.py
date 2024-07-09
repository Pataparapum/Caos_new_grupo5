from django.contrib import admin
from django.urls import path, include

from RegisterAndLogin.forms import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', include('caosnoticias.urls')),
    path('sesion/', include('RegisterAndLogin.urls')),
<<<<<<< HEAD
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye esta línea
=======

>>>>>>> 883add300c7b5dd879efc4f48bb5a6d8fed3f527
]
