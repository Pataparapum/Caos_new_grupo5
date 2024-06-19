# tu_app_noticias/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('noticias_Climaticas/', views.noticias_Climaticas, name='noticias_Climaticas'),
]
