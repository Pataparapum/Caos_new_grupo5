from django import forms
from .models import Noticia, Imagen

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'ubicacion', 'categoria']
        widgets = {
            'categoria': forms.Select(choices=Noticia.CATEGORIAS),
        }

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen']
