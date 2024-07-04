# tu_app_noticias/views.py
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'noticias/index.html', context)

def noticias_Climaticas(request):
    context = {}
    return render(request, 'noticias/noticias_Climaticas.html', context)

def noticiasCienciayTecnologia(request):
    context = {}
    return render(request, 'noticias/noticiasCienciayTecnologia.html', context)
def noticiasInternacionales(request):
    context = {}
    return render(request, 'noticias/noticiasInternacionales.html', context)
def noticiasdeportes(request):
    context = {}
    return render(request, 'noticias/noticiasdeportes.html', context)
def noticiaseconomia(request):
    context = {}
    return render(request, 'noticias/noticiaseconomia.html', context)


