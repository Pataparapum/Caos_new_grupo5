from django.shortcuts import render
from .models import ReadUser, WriteUser
from .forms import Reader, Writer

# Create your views here.+
def register(request):
    form = Reader()
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
            
            UserW = WriteUser.objects.all();
            
        return render(request, "crearCuenta.html", context)


def login(request):
    context = {}
    return render(request, "inicioSesion.html", context)

def prueba(request):
    if request.method == "POST":
        value = request.POST["type"]
        context = {
            'post': value
        }
    else:
        return render(request, "prueba.html")
    return render(request, "prueba.html", context)
