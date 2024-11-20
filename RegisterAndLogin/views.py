from django.contrib.messages import constants as messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .funciones import *
from .forms import ChangePassword, ChangeUserName
from .models import ReadUser, WriteUser


logger = logging.getLogger(__name__)

def register(request):
    if request.method != 'POST': return redirect('index')
    
    
    userType = request.POST["type"]
    context = {}


    if userType == "write" or userType == "read": return typeForm(request, userType, context);
        
    if userType == "createwrite": return writeUserCase(request)
                    
    if userType == "createread": return readUserCase(request)
                

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


def tipoUser(request):
    if(request.method != "POST"):
        return render(request, "tipoUser.html")

@login_required
def CambiarUsername(request):
    if (request.method != 'POST'):
        form = ChangeUserName()
        context = {
            'form':form
        }
        return render(request, 'cambiarUsername.html', context)
    username = request.user.username
    typeUser = User.objects.filter(username=username).first().first_name
    newUsername = request.POST['newUsername']
    cNewUsername = request.POST['CnewUserName']
    
    if (userExist(newUsername)):
        form = ChangeUserName()
        mensaje = 'usuario ya registrado'
        context = {
            'form':form,
            'error':mensaje
        }
        return render(request, 'cambiarUsername.html', context)
    
    if (newUsername == cNewUsername):
        if (typeUser == 'write'):
            writeU = WriteUser.objects.get(userName=username)
            user = User.objects.get(username=username)
            writeU.userName = newUsername
            user.username = newUsername
            user.save()
            writeU.save()
            
            login(request, user)
            return redirect('index')
        elif (typeUser == 'read'):
            readU = ReadUser.objects.get(userName=username)
            user = User.obects.get(username=username)
            readU.userName = newUsername
            user.username = newUsername
            user.save()
            writeU.save()
            
            login(request, user)
            return redirect('index')
        else:
            user = User.objects.get(username=username)
            user.username = newUsername
            user.save()
    else:
        form = ChangeUserName()
        mensaje = 'Los campos no coinciden'
        context = {
            'form':form,
            'error':mensaje
        }
        return render(request, 'cambiarUsername.html', context)          

@login_required
def cambiarPassword(request):
    if (request.method != 'POST'):
        form = ChangePassword()
        context = {
            'form':form
        }
        return render(request, 'cambiarPassword.html', context);
    
    oldP = request.POST['oldPassword']
    newP = request.POST['newPassword']
    cNewP = request.POST['newPasswordC']
    username = request.user.username
    
    if (oldPasswordCorrect(oldP, username)):
        
        if (newP == cNewP):    
            user = User.objects.get(username=username)
            user.set_password(newP)
            user.save()
            login(request, user)
            return redirect('index')
        
        else:
            form = ChangePassword()
            mensaje = "los campos no coinciden"
            context = {
                'form':form,
                'error':mensaje
            }
            return render(request, 'cambiarPassword.html', context)
    else:
        form = ChangePassword()
        mensaje = "la contraseña antigua es incorrecta"
        context = {
            'form':form,
            'error':mensaje
        }
        return render(request, 'cambiarPassword.html', context)
    
@login_required
def deleteAccount(request):
    username = request.user.username
    return deleteUser(request, username)
    

@login_required
def deleteUser(request, username):
    try:
        user = User.objects.get(username=username)
        if(WriteUserExist(user)):
            write = WriteUser.objects.get(userName=username)
            write.delete()
            user.delete()
            logger.warning('escritor borrado')
            
            return redirect('usuarios')
        
        elif (ReadUserExist(user)):
            read = ReadUser.objects.get(userName=username)
            read.delete()
            user.delete()

            logger.warning('lector borrado')

            return redirect('usuarios')
        
        else:
            logger.warning('no paso nada')
            logout(request)
            user.delete()

            return redirect('usuarios')
    
    except User.DoesNotExist:
        messages.error(request, 'El usuario no existe')
        return redirect('usuarios')
        
    except Exception as e:
        messages.error(request, e)
        return redirect('usuarios')

def usuarios(request):
    usuarios = User.objects.filter(first_name="read") | User.objects.filter(first_name="write")

    context = {
        "user": usuarios
    }

    return render(request, 'usuario.html', context)