from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from subir_noticias.models import Noticia
from .forms import ContactoForm
from .models import Contacto
from RegisterAndLogin.models import ReadUser, WriteUser



def index(request):
    try:
        ultima_noticia = Noticia.objects.latest('fecha_publicacion')
    except Noticia.DoesNotExist:
        ultima_noticia = None

    context = {
        'usuario': request.user.username,
        'ultima_noticia': ultima_noticia,
    }
    return render(request, 'noticias/index.html', context)

@login_required
def mensajes_recibidos(request):
    mensajes = Contacto.objects.all()
    return render(request, 'noticias/mensajes_recibidos.html', {'mensajes': mensajes})


@login_required
def userCenter(request):
    return render(request,'userCenter/userCenter.html')

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

@login_required
def userCenter(request):
    user = request.user.username
    context = {}
    if (WriteUser.objects.filter(userName=user)):
        typeUser = request.user.first_name
        context = {
            'typeU':typeUser
        }
        return render(request, 'userCenter/userCenter.html', context)
    elif(ReadUser.objects.filter(userName=user)):
        typeUser =request.user.first_name
        context = {
            'typeU': typeUser
        }
        return render(request, 'userCenter/userCenter.html', context)
    else:
        typeUser = 'admin'
        context = {
            'typeU': typeUser
        }
        return render(request,'userCenter/userCenter.html', context)

def noticias_policial(request):
    return render(request, 'noticias/noticias_policial.html')

def formulario_exitoso(request):
    return render(request, 'noticias/formulario_exitoso.html')

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_exitoso')
    else:
        form = ContactoForm()
    return render(request, 'noticias/contacto.html', {'form': form})
