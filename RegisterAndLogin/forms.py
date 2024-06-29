from django import forms
from .models import ReadUser, WriteUser
from django.forms import ModelForm

class Reader(forms.Form):
    nombre = forms.CharField(label="* User name", max_length=50, required=True,
                             widget=forms.TextInput(
                                 attrs={'class':'inputform form-control',
                                        'id': 'user',
                                        'placeholder': 'user',
                                        'name':'user'}
                             ))
    email = forms.EmailField(label="* Email", max_length=50, required=True,
                             widget=forms.EmailInput(
                                 attrs={'class':'inputform form-control',
                                        'id':'email',
                                        'placeholder':'name@example.com',
                                        'name':'email'
                                 }
                             ))
    password = forms.CharField(label="*password", max_length=50, required=True,
                               widget=forms.PasswordInput(
                                   attrs={'class':'inputform form-control',
                                          'id':'password',
                                          'placeholder':'password',
                                          'name':'password'}
                               ))
    
    
class Writer(forms.Form):
    nombre = forms.CharField(label="* User name", max_length=50, required=True,
                             widget=forms.TextInput(
                                 attrs={'class':'inputform form-control',
                                        'id': 'user',
                                        'placeholder': 'user',
                                        'name':'user'}
                             ))
    email = forms.EmailField(label="* Email", max_length=50, required=True,
                             widget=forms.EmailInput(
                                 attrs={'class':'inputform form-control',
                                        'id':'email',
                                        'placeholder':'name@example.com',
                                        'name':'email'
                                 }
                             ))
    password = forms.CharField(label="* password", max_length=50, required=True,
                               widget=forms.PasswordInput(
                                   attrs={'class':'inputform form-control',
                                          'id':'password',
                                          'placeholder':'password',
                                          'name':'password'}
                               ))
    empresa = forms.CharField(label="* empresa", max_length=50, required=True,
                              widget=forms.TextInput(
                                  attrs={'class':'inputform form-control',
                                         'id':'empresa',
                                         'placeholder':'empresa',
                                         'name':'empresa'}
                              ))