from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from subir_noticias.models import Noticia, Imagen
from .forms import ContactoForm
from .models import Contacto
from RegisterAndLogin.models import ReadUser, WriteUser


def index(request):
    try:
        ultima_noticia = Noticia.objects.filter(aprobada=True).latest('fecha_publicacion')
    except Noticia.DoesNotExist:
        ultima_noticia = None
    imagenUrl = Imagen.objects.get(id=ultima_noticia.id).imagen
    context = {
        'usuario': request.user.username,
        'imagenU': imagenUrl,
        'ultima_noticia': ultima_noticia,
    }
    return render(request, 'noticias/index.html', context)


@login_required
def mensajes_recibidos(request):
    mensajes = Contacto.objects.all()
    return render(request, 'noticias/mensajes_recibidos.html', {'mensajes': mensajes})


@login_required
def userCenter(request):
    user = request.user.username
    context = {}
    if WriteUser.objects.filter(userName=user).exists():
        typeUser = request.user.first_name
        context = {
            'typeU': typeUser
        }
    elif ReadUser.objects.filter(userName=user).exists():
        typeUser = request.user.first_name
        context = {
            'typeU': typeUser
        }
    else:
        typeUser = 'admin'
        context = {
            'typeU': typeUser
        }
    return render(request, 'userCenter/userCenter.html', context)


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

@login_required
@require_POST
def eliminar_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Contacto, id=mensaje_id)
    mensaje.delete()
    return redirect('mensajes_recibidos')
