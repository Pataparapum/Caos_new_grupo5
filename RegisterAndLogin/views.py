from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import Reader, Writer

# Create your views here.

def register(request):
    if (request.method != 'POST'):
        return redirect('index')
    
    userType = request.POST["type"]
    context = {}
    
    if (request.POST["type"] == "write"):
        form = Writer()
        context = {
            'form':form,
            'user':userType
        }
        
        return render(request, "crearCuenta.html", context)
    
    elif (request.POST["type"] == "read"):
        form = Reader()
        context = {
            'form':form,
            'user':userType
        }
        
        return render(request, "crearCuenta.html", context)
        
    else:
        if (userType == "createwrite"):
            form = Writer(request.POST)
            if form.is_valid():
                try:
                    validate_email(request.POST['email'])
                except ValidationError:
                    form = Writer()
                    mensaje = 'Formato de email invalido'
                    context = {
                        'form' : form,
                        'mensaje' : mensaje,
                        'user' : 'write'
                    }
                    return render (request, 'crearCuenta.html', context)
                    
                else:
                    form.save()
                    form = Writer()
                    return redirect('index')
            else:
                form = Writer()
                mensaje = 'los datos no son validos'
                context = {
                    'mensaje': mensaje,
                    'form':form,
                    'user':'write'
                }
                return render(request, 'crearCuenta.html', context)
                    
        elif (userType == "createread"):
            form = Reader(request.POST)
            if form.is_valid():
                try:
                    validate_email(request.POST['email'])
                except ValidationError:
                    form = Reader()
                    mensaje = 'Formato de email invalido'
                    context = {
                        'form' : form,
                        'mensaje' : mensaje,
                        'user' : 'read'
                    }
                    return render (request, 'crearCuenta.html', context)
                    
                else:
                    form.save()
                    form = Reader()
                    return redirect('index')
            else:
                form = Writer()
                mensaje = 'los datos no son validos'
                context = {
                    'mensaje': mensaje,
                    'form':form,
                    'user':'write'
                }
                return render(request, 'crearCuenta.html', context)
                
    return render(request, 'crearCuenta.html', context)


def login(request):
    context = {}
    return render(request, "inicioSesion.html", context)

def prueba(request):
    
    
    if(request.method != "POST"):
        return render(request, "prueba.html")
    else:
        value = request.POST["type"]
        context = {
            'post':value
        }
        return render(request, "prueba.html", context)