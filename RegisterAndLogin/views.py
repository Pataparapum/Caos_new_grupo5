from django.shortcuts import render

# Create your views here.+
def register(request):
    context = {}
    return render(request, "crearCuenta.html", context)

def login(request):
    context = {}
    return render(request, "inicioSesion.html", context)
    