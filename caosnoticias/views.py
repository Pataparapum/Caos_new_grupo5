# tu_app_noticias/views.py
from django.shortcuts import render
from django.contrib.auth import logout

def index(request):
    if (request.method == 'POST' ):
        logout(request)
        del request.session['usuario']
    if (request.user.is_authenticated):
        
            request.session['usuario']=request.user.username
            user = request.session['usuario']
            context = {
                'user':user
            }
            return render(request, 'noticias/index.html', context)
    else :
        context = {}
        return render(request,'noticias/index.html', context)
    
    

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
