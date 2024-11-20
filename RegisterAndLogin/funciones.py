from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
import logging

from RegisterAndLogin.forms import Reader, Writer
from .models import ReadUser, WriteUser

logger = logging.getLogger(__name__)

def userExist(username):
    return User.objects.filter(username=username).count() > 0

def ReadUserExist(username):
    return ReadUser.objects.filter(userName=username).count() > 0

def WriteUserExist(username):
    return WriteUser.objects.filter(userName=username).count() > 0

def oldPasswordCorrect(old, user):
    password = User.objects.filter(username=user).first().password
    print(password)
    return check_password(old, password)

def typeForm(request, userType, context):
    if (userType == "write"):
        form = Writer()
        context = {
            'form':form,
            'user':userType
        }
        
        return render(request, "crearCuenta.html", context)
    
    elif (userType == "read"):
        form = Reader()
        context = {
            'form':form,
            'user':userType
        }
        
        return render(request, "crearCuenta.html", context)
    
def writeUserCase(request):
    try:
        validate_email(request.POST['email'])
    except ValidationError:
        form = Writer()
        mensaje = 'Formato de email invalido'
        context = {
            'form' : form,
            'error' : mensaje,
            'user' : 'write'
        }
        return render (request, 'crearCuenta.html', context)
            
    form = Writer(request.POST)
    if form.is_valid() and not WriteUserExist(request.POST['userName']):
                
        form.save()
                
        user = User.objects.create_user(form.cleaned_data['userName'], form.cleaned_data['email'], request.POST['password'])
        user.first_name = "write"
        user.has_perm('RegisterAndLogin.view_Newspaper')
        user.has_perm('RegisterAndLogin.add_Newspaper')
        user.has_perm('RegisterAndLogin.delete_Newspaper')
        user.has_perm('RegisterAndLogin.change_Newspaper')
        user.has_perm('RegisterAndLogin.delete_WriteUser')
        user.has_perm('RegisterAndLogin.change_WriteUser')
        user.save()
                
        login(request, user)
                    
        form = Writer()
        return redirect('index')
    else:
        form = Writer()
        mensaje = 'los datos no son validos o el usuario ya esta registrado'
        context = {
            'error': mensaje,
            'form':form,
            'user': 'write'
        }
        return render(request, 'crearCuenta.html', context)
    
def readUserCase(request):
    try:
        validate_email(request.POST['email'])
    except ValidationError:
        form = Reader()
        mensaje = 'Formato de email invalido'
        context = {
            'form' : form,
            'error' : mensaje,
            'user' : 'read'
        }
        return render(request, 'crearCuenta.html', context)
            
    form = Reader(request.POST)

    if form.is_valid() and not ReadUserExist(request.POST['userName']):
        form.save()
                    
        user = User.objects.create_user(form.cleaned_data['userName'], form.cleaned_data['email'], request.POST['password'])
        user.first_name = 'read'
        user.has_perm('RegisterAndLogin.view_Newspaper')
        user.has_perm('RegisterAndLogin.delete_ReadUser')
        user.has_perm('RegisterAndLogin.change_ReadUser')
        user.save()
                
        login(request, user)
                
        form = Reader()
        return redirect('index')
            
    else:
        form = Reader()
        mensaje = 'los datos no son validos o el usuario ya esta registrado'
        context = {
            'error': mensaje,
            'form': form,
            'user': 'read'
        }
        return render(request, 'crearCuenta.html', context)
    
def deleteUser(request, username):
    try:
        user = User.objects.get(username=username)
        if(WriteUserExist(user)):
            write = WriteUser.objects.get(userName=username)
            logout(request)
            write.delete()
            user.delete()
            return redirect('index')
        
        elif (ReadUserExist(user)):
            read = ReadUser.objects.get(userName=username)
            logout(request)
            read.delete()
            user.delete()
            return redirect('index')
        
        else:
            logout(request)
            user.delete()
            return redirect('index')
    
    except User.DoesNotExist:
        messages.error(request, 'El usuario no existe')
        
    except Exception as e:
        messages.error(request, e)

