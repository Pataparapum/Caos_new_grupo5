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
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('newPassword/', views.PasswordChangeView.as_view(
        template_name="cambiarPassword.html"
    ),
         name='newPassword'),
    path('newUsername/', newUsername, name='newUsername'),
]
