from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from RegisterAndLogin.funciones import  WriteUserExist
from .models import Noticia, Imagen
from .forms import NoticiaForm, ImagenForm

@login_required
def subir_noticia(request):
    if (request.user.first_name != 'write' and not WriteUserExist):
        return redirect('index')
    if request.method == 'POST':
        noticia_form = NoticiaForm(request.POST)
        imagen_form = ImagenForm(request.POST, request.FILES)
        if noticia_form.is_valid() and imagen_form.is_valid():
            noticia = noticia_form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            imagen = imagen_form.save(commit=False)
            imagen.noticia = noticia
            imagen.save()
            return redirect('confirmacion')
    else:
        noticia_form = NoticiaForm()
        imagen_form = ImagenForm()
    return render(request, 'subir_noticias/subir_noticia.html', {'noticia_form': noticia_form, 'imagen_form': imagen_form})

@login_required
def confirmacion(request):
    return render(request, 'subir_noticias/confirmacion.html')

@login_required
def revisar_noticias(request):
    if (request.user.first_name == 'write' or request.user.first_name == 'read'):
        return redirect('index')
    noticias = Noticia.objects.filter(aprobada=False, rechazada=False)
    return render(request, 'subir_noticias/revisar_noticias.html', {'noticias': noticias})

@login_required
def aprobar_noticia(request, noticia_id):
    if (request.user.first_name == 'write' or request.user.first_name == 'read'):
        return redirect('index')
    noticia = get_object_or_404(Noticia, id=noticia_id)
    noticia.aprobada = True
    noticia.rechazada = False
    noticia.motivo_rechazo = ''
    noticia.publicada = True  # Marcar como publicada
    noticia.save()
    return redirect('revisar_noticias')

def rechazar_noticia(request, noticia_id):
    if (request.user.first_name == 'write' or request.user.first_name == 'read'):
        return redirect('index')
    noticia = get_object_or_404(Noticia, id=noticia_id)
    
    if request.method == 'POST':
        motivo_rechazo = request.POST.get('motivo', '')
        noticia.motivo_rechazo = motivo_rechazo
        noticia.rechazada = True
        noticia.save()
        noticia.delete()  # Elimina la noticia de la base de datos
        return redirect('noticias_publicadas')
    
    return render(request, 'subir_noticias/rechazar_noticia.html', {'noticia': noticia})

@login_required(login_url='/subir_noticias/registro/')
def ver_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    imagenes = Imagen.objects.filter(noticia=noticia)
    return render(request, 'subir_noticias/ver_noticia.html', {'noticia': noticia, 'imagenes': imagenes})

@login_required
def perfil_usuario(request):
    noticias = Noticia.objects.filter(autor=request.user)
    return render(request, 'subir_noticias/perfil_usuario.html', {'noticias': noticias})


def noticias_publicadas(request):
    noticias = Noticia.objects.filter(aprobada=True, publicada=True)
    return render(request, 'subir_noticias/noticias_publicadas.html', {'noticias': noticias})

def ver_noticia_publicada(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id, aprobada=True, publicada=True)
    imagenes = Imagen.objects.filter(noticia=noticia)
    return render(request, 'subir_noticias/ver_noticia_publicada.html', {'noticia': noticia, 'imagenes': imagenes})

def registro(request):
    return render(request, 'subir_noticias/registro.html')