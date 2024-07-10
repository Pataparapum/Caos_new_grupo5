from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('subir/', views.subir_noticia, name='subir_noticia'),
    path('revisar/', views.revisar_noticias, name='revisar_noticias'),
    path('rechazar/<int:noticia_id>/', views.rechazar_noticia, name='rechazar_noticia'),
    path('ver/<int:noticia_id>/', views.ver_noticia, name='ver_noticia'),
    path('aprobar/<int:noticia_id>/', views.aprobar_noticia, name='aprobar_noticia'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('confirmacion/', TemplateView.as_view(template_name='subir_noticias/confirmacion.html'), name='confirmacion'),
]
