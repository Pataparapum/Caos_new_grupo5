from django.urls import path
from .views import *
from django.contrib.auth import views
from .forms import UserLoginForm

urlpatterns = [
    path('register/', register, name="register"),
    path('prueba/', prueba, name='prueba'),
    path('login/', views.LoginView.as_view(
        template_name="login.html",
        authentication_form=UserLoginForm
    ),
         name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
