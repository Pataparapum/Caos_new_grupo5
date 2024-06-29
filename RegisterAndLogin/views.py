from django.shortcuts import render
from .forms import Reader

# Create your views here.+
def register(request):
    form = Reader()
    context = {}
    
    if (request.method != "POST"):
        context = {
            'form': form
        }
        return render(request, "crearCuenta.html", context)
    else:
        lista = []
        lista.append(request.POST["user"])
        lista.append(request.POST["email"])
        lista.append(request.POST["password"])
        
        context = {'hola': lista,
                   'form':form}
        return render(request, "crearCuenta.html", context)

def login(request):
    context = {}
    return render(request, "inicioSesion.html", context)

def prueba(request):
    return render(request, "prueba.html")