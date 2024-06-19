# tu_app_noticias/views.py
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'noticias/index.html', context)

def noticias_Climaticas(request):
    context = {}
    return render(request, 'noticias/noticias_Climaticas.html', context)
