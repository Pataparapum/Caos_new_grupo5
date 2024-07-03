from django import forms
from .models import ReadUser, WriteUser
from django.forms import ModelForm

class Reader(forms.Form, ModelForm):
    
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
        