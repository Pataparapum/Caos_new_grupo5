from django.urls import path
from .views import *
from django.contrib.auth import views
from .forms import UserLoginForm

urlpatterns = [
    path('register/', register, name="register"),
    path('typeUser/', tipoUser, name='typeUser'),
    path('login/', views.LoginView.as_view(
        template_name="login.html",
        authentication_form=UserLoginForm
    ),
         name='login'),
    path('logout/', logout_view, name='logout'),
    path('newPassword/', cambiarPassword, name='newPassword'),
    path('newUsername/', CambiarUsername, name='newUsername'),
    path('deleteAccount/', deleteAccount, name="deleteAccount"),
    path('usuarios/', usuarios, name='usuarios'),
    path('deleteUser/<username>', deleteUser, name='deleteUser')
]
