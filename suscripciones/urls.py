from django.urls import path
from .views import suscribirse, view_cart, remove_from_cart

urlpatterns = [
    path('suscribirse/', suscribirse, name='suscribirse'),
    path('carrito/', view_cart, name='view_cart'),
    path('carrito/remove/<int:index>/', remove_from_cart, name='remove_from_cart'),
]
