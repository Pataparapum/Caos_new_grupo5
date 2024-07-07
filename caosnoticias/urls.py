from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include


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
    path('ver_mensajes/', views.ver_mensajes, name='ver_mensajes'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('periodistas/', views.periodistas, name='periodistas'),
    
]

