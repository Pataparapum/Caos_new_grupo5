from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import ReadUser, WriteUser
from django.contrib.auth.hashers import *

class Reader(forms.Form, ModelForm):
    
    class Meta:
        model = ReadUser
        fields = ["userName", "email"]
        labels = {
            "userName" : "* User Name",
            "email" : "* Email",
        }
        widgets = {
            "userName" : forms.TextInput(
                                 attrs={'class':'inputform form-control',
                                        'id': 'user',
                                        'placeholder': 'user',
                                        'name': 'userName'
                                        }),
            "email" : forms.EmailInput(
                                 attrs={'class':'inputform form-control',
                                        'id':'email',
                                        'placeholder':'name@example.com',
                                        'name': 'email'
                                        }),
            
        }
    
    
class Writer(forms.Form, ModelForm):

    
    class Meta:
        model = WriteUser
        fields = ['userName', 'email', 'empresa']
        labels = {
            "userName" : "* User Name",
            "email" : "* Email",
            "empresa" : "* Empresa",
        }
        widgets = {
            "userName" : forms.TextInput(attrs={'class':'inputform form-control',
                                        'id': 'user',
                                        'placeholder': 'user',
                                        'name': "userName"
                                    }),
            "email" : forms.EmailInput(
                                 attrs={'class':'inputform form-control',
                                        'id':'email',
                                        'placeholder':'name@example.com',
                                        'name': "email"
                                        }),
            "empresa" : forms.TextInput(
                                  attrs={'class':'inputform form-control',
                                         'id':'empresa',
                                         'placeholder':'empresa',
                                         'name': 'empresa'
                                         }),
        }
        
class ChangeUserName(forms.Form):
    
    newUsername = forms.CharField(label='New username', required=True, widget=forms.TextInput(
        attrs={
            'class':'inputform form-control',
            'id':'newusername',
            'placeholder':'nuevo nombre de usuario',
            'name': 'newuserName'
        }
    ))
    
    CnewUserName = forms.CharField(label='Confirm New Username', required=True, widget=forms.TextInput(
        attrs={
            'class':'inputform form-control',
            'id':'cnewusername',
            'placeholder':'confirmar nombre de usuario',
            'name': 'cuserName'
        }
    ))
        
class ChangePassword(forms.Form):
    
    oldPassword = forms.CharField(label="Contraseña Antigua", required=True, widget=forms.PasswordInput(
        attrs={
            'class':'inputform form-control',
            'id':'oldpassword',
            'placeholder':'old password',
            'name': 'oldPassword'
        }
    ))
    
    newPassword = forms.CharField(label="Nueva Contraseña", required=True, widget=forms.PasswordInput(
        attrs={
            'class':'inputform form-control',
            'id':'newpassword',
            'placeholder':'new password',
            'name': 'newPassword'
        }
    ))
    
    newPasswordC = forms.CharField(label="Confirmar Contraseña", required=True, widget=forms.PasswordInput(
        attrs={
            'class':'inputform form-control',
            'id':'newpasswordc',
            'placeholder':'confirmar password',
            'name': 'newPasswordC'
        }
    ))
    
class UserLoginForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)
        
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                ("This account is inactive."),
                code="inactive",
            )
    
    def get_user(self) -> User:
        return super().get_user()
    
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class':'inputform form-control',
            'placeholder': 'username',
            'id':'user',
            'name': 'userName'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'inputform form-control',
            'placeholder':'password',
            'id':'password',
            'name': 'password'
        }
    ))