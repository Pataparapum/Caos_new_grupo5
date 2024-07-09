from django.contrib import admin
from django.urls import path, include

from RegisterAndLogin.forms import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', include('caosnoticias.urls')),
    path('sesion/', include('RegisterAndLogin.urls')),
]
