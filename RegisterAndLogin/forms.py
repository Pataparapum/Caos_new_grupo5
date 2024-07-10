from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import ReadUser, WriteUser
from django.contrib.auth.hashers import *

class Reader(forms.Form, ModelForm):
    
    def clean_password(self):
        data = self.cleaned_data['password']
        hashPassword = make_password(data)
        return hashPassword
    
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
                                        'placeholder': 'user'
                                        }),
            "email" : forms.EmailInput(
                                 attrs={'class':'inputform form-control',
                                        'id':'email',
                                        'placeholder':'name@example.com'
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
                                        'placeholder': 'user'
                                    }),
            "email" : forms.EmailInput(
                                 attrs={'class':'inputform form-control',
                                        'id':'email',
                                        'placeholder':'name@example.com'
                                        }),
            "empresa" : forms.TextInput(
                                  attrs={'class':'inputform form-control',
                                         'id':'empresa',
                                         'placeholder':'empresa'
                                         }),
        }
    
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
            'id':'user'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'inputform form-control',
            'placeholder':'password',
            'id':'password'
        }
    ))