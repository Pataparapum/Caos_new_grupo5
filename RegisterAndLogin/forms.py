from typing import Any
from django import forms
from .models import ReadUser, WriteUser
from django.forms import ModelForm
from django.contrib.auth.hashers import *

class Reader(forms.Form, ModelForm):
    
    def clean_password(self):
        data = self.cleaned_data['password']
        hashPassword = make_password(data)
        return hashPassword
    
    class Meta:
        model = ReadUser
        fields = ["userName", "email", "password"]
        labels = {
            "userName" : "* User Name",
            "email" : "* Email",
            "password" : "* Password"
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
            "password" : forms.PasswordInput(
                                   attrs={'class':'inputform form-control',
                                          'id':'password',
                                          'placeholder':'password',
                                          'name':'password'
                                          })
            
        }
    
    
class Writer(forms.Form, ModelForm):

    
    def clean_password(self):
        data = self.cleaned_data['password']
        hashPassword = make_password(data)
        return hashPassword
    
    class Meta:
        model = WriteUser
        fields = ['userName', 'email', 'empresa', 'password']
        labels = {
            "userName" : "* User Name",
            "email" : "* Email",
            "empresa" : "* Empresa",
            "password" : "* Password"
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
            "password" : forms.PasswordInput(
                                   attrs={'class':'inputform form-control',
                                          'id':'password',
                                          'placeholder':'password'
                                          })
        }
    