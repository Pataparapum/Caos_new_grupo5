from django.urls import path
from .views import suscribirse, view_cart, remove_from_cart, realizar_compra, resumen_pedido

urlpatterns = [
    path('suscribirse/', suscribirse, name='suscribirse'),
    path('carrito/', view_cart, name='view_cart'),
    path('carrito/remove/<int:index>/', remove_from_cart, name='remove_from_cart'),
    path('realizar_compra/', realizar_compra, name='realizar_compra'),
    path('resumen_pedido/', resumen_pedido, name='resumen_pedido'),
]

    
