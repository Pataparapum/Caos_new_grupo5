# subir_noticias/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('subir/', views.subir_noticia, name='subir_noticia'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('revisar/', views.revisar_noticias, name='revisar_noticias'),
    path('aprobar/<int:noticia_id>/', views.aprobar_noticia, name='aprobar_noticia'),
    path('rechazar/<int:noticia_id>/', views.rechazar_noticia, name='rechazar_noticia'),
    path('ver/<int:noticia_id>/', views.ver_noticia, name='ver_noticia'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('noticias/publicadas/', views.noticias_publicadas, name='noticias_publicadas'),
    path('noticia/<int:noticia_id>/', views.ver_noticia_publicada, name='ver_noticia_publicada'),
    path('registro/', views.registro, name='registro'),
    
]
