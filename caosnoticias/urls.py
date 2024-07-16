# caosnoticias/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
    path('index/', views.index, name='index'),
    path('noticias_climaticas/', views.noticias_climaticas, name='noticias_climaticas'),
    path('noticias_ciencia_tecnologia/', views.noticias_ciencia_tecnologia, name='noticias_ciencia_tecnologia'),
    path('noticias_economia/', views.noticias_economia, name='noticias_economia'),
    path('noticias_internacionales/', views.noticias_internacionales, name='noticias_internacionales'),
    path('noticias_deportes/', views.noticias_deportes, name='noticias_deportes'),
    path('noticias_fisica_cuantica/', views.noticias_fisica_cuantica, name='noticias_fisica_cuantica'),
    path('formulario_exitoso/', views.formulario_exitoso, name='formulario_exitoso'),
    path('periodistas/', views.periodistas, name='periodistas'),
    path('user/', views.userCenter, name='userCenter'),
    path('noticias_policial/', views.noticias_policial, name='noticias_policial'),
    path('contacto/', views.contacto, name='contacto'),
    path('mensajes_recibidos/', views.mensajes_recibidos, name='mensajes_recibidos'),
    path('mensajes_recibidos/eliminar/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
]
