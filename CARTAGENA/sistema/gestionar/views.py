from django.shortcuts import render
from django.http import HttpResponse
from .models import matriculaEscolar

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Hola</h1>")

def pobreza(request):
    return render(request, 'paginas/pobreza.html')

def educacion(request):
    educacion = matriculaEscolar.objects.all()
    return render(request, "paginas/educacion.html", {'educacion': educacion})

def empleo(request):
    return render(request, 'paginas/empleo.html')

def movilidad(request):
    return render(request, 'paginas/movilidad.html')

def seguridad(request):
    return render(request, 'paginas/seguridad.html')