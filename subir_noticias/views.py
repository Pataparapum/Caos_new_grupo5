from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Noticia, Imagen
from .forms import NoticiaForm, ImagenForm

@login_required
def subir_noticia(request):
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

@user_passes_test(lambda u: u.is_staff)
def revisar_noticias(request):
    noticias = Noticia.objects.filter(aprobada=False, rechazada=False)
    return render(request, 'subir_noticias/revisar_noticias.html', {'noticias': noticias})

@user_passes_test(lambda u: u.is_staff)
def aprobar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    noticia.aprobada = True
    noticia.save()
    return redirect('revisar_noticias')

@user_passes_test(lambda u: u.is_staff)
def rechazar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        motivo = request.POST.get('motivo')
        noticia.rechazada = True
        noticia.motivo_rechazo = motivo
        noticia.save()
        return redirect('revisar_noticias')
    return render(request, 'subir_noticias/rechazar_noticia.html', {'noticia': noticia})

@user_passes_test(lambda u: u.is_staff)
def ver_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    imagenes = Imagen.objects.filter(noticia=noticia)
    return render(request, 'subir_noticias/ver_noticia.html', {'noticia': noticia, 'imagenes': imagenes})

@login_required
def perfil_usuario(request):
    noticias = Noticia.objects.filter(autor=request.user)
    return render(request, 'subir_noticias/perfil_usuario.html', {'noticias': noticias})
