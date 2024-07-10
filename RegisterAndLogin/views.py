from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from .forms import Reader, Writer, UserPasswordChangeForm
from .models import ReadUser, WriteUser



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
                    
                    user = User.objects.create_user(form.cleaned_data['userName'], form.cleaned_data['email'], form.cleaned_data['password'])
                    user.has_perm('RegisterAndLogin.view_Newspaper')
                    user.has_perm('RegisterAndLogin.add_Newspaper')
                    user.has_perm('RegisterAndLogin.dalate_Newspaper')
                    user.has_perm('RegisterAndLogin.change_Newspaper')
                    user.save()
                
                    login(request, user)
                    
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
                    
                    user = User.objects.create_user(form.cleaned_data['userName'], form.cleaned_data['email'], form.cleaned_data['password'])
                    user.has_perm('RegisterAndLogin.view_Newspaper')
                    
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

def tipoUser(request):

    if(request.method != "POST"):
        return render(request, "tipoUser.html")

def newUsername(request):
    return render(request, 'cambiarUsername.html')

def modelPassword(request):
    if (request.method == "POST"):
        user = request.user.username
        read = ReadUser.objects.all().filter(userName=user)
        write = WriteUser.objects.all().filter(userName=user)
        if (read):
            read.password = request.user.password
            read.save()
        elif (write):
            write.passwrod = request.user.password
            write.save()
        return redirect('index')
    else:
        return redirect('index')