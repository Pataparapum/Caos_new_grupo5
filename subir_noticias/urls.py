# urls.py
from django.urls import path
from .views import subir_noticia, revisar_noticias, aprobar_noticia, rechazar_noticia, ver_noticia, perfil_usuario, noticias_publicadas, ver_noticia_publicada

urlpatterns = [
    path('subir/', subir_noticia, name='subir_noticia'),
    path('revisar/', revisar_noticias, name='revisar_noticias'),
    path('aprobar/<int:noticia_id>/', aprobar_noticia, name='aprobar_noticia'),
    path('rechazar/<int:noticia_id>/', rechazar_noticia, name='rechazar_noticia'),
    path('ver/<int:noticia_id>/', ver_noticia, name='ver_noticia'),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('publicadas/', noticias_publicadas, name='noticias_publicadas'),
    path('publicada/<int:noticia_id>/', ver_noticia_publicada, name='ver_noticia_publicada'),
]
