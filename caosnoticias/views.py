from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactoForm
from .models import ContactoFormModel

def index(request):
    return render(request, 'noticias/index.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje fue enviado con éxito.')
            return redirect('formulario_exitoso')
        else:
            messages.error(request, 'Error en el formulario. Por favor corrige los errores.')
    else:
        form = ContactoForm()
    return render(request, 'noticias/contacto.html', {'form': form})

@login_required
def formulario_exitoso(request):
    return render(request, 'noticias/formulario_exitoso.html')

@login_required
def ver_mensajes(request):
    mensajes = ContactoFormModel.objects.all()
    return render(request, 'noticias/ver_mensajes.html', {'mensajes': mensajes})

def noticias_climaticas(request):
    return render(request, 'noticias/noticias_climaticas.html')

def noticias_economia(request):
    return render(request, 'noticias/noticias_economia.html')

def noticias_ciencia_tecnologia(request):
    return render(request, 'noticias/noticias_ciencia_tecnologia.html')

def noticias_internacionales(request):
    return render(request, 'noticias/noticias_internacionales.html')

def noticias_deportes(request):
    return render(request, 'noticias/noticias_deportes.html')

def noticias_fisica_cuantica(request):
    return render(request, 'noticias/noticias_fisica_cuantica.html')

def periodistas(request):
    return render(request, 'noticias/periodistas.html')

