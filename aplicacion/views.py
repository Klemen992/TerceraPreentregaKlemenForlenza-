from django.shortcuts import render
from .models import *
from .forms import PlantasForm
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")   #Significa que cuando te llega una peticion, la redirijas a una pagina




def plantas(request):                               #contexto' es un diccionario, 'plants' es su clave
    contexto = {'plants':Plantas.objects.all(), "Titel": "disponible", "descuento": ["4 por 3", "20% pagando en efectivo"]}      #Plantas' es el modelo, dice que me devuelva todos los objetos de la clase o modelo Plantas
    return render(request, "aplicacion/plants.html", contexto)


def plantasForm(request):
    if request.method == "POST":
        plantas = Plantas(especie=request.POST['especie'],
                          genero=request.POST['genero'],
                          precio=request.POST['precio'])
        plantas.save()
        return HttpResponse ("Se agrego al carrito")
    return render(request, "aplicacion/plantsForm.html")


def plantasForm2(request):
    if request.method == "POST":
        miForm = PlantasForm(request.POST)      #miForm es una variable
        if miForm.is_valid():
            plantas_especie = miForm.cleaned_data.get('especie')
            plantas_genero= miForm.cleaned_data.get('genero')     #plantas_especie es una variable
            plantas_precio = miForm.cleaned_data.get('precio')
            plantas = Plantas (especie = plantas_especie,
                               genero = plantas_genero,       #plantas es un objeto, Plantas es el modelo
                               precio = plantas_precio)
            plantas.save()
            return render(request, "aplicacion/base.html")   
    else:
        miForm = PlantasForm()          #PlantasForm es una clase
    return render(request, "aplicacion/plantsForm2.html", {"form": miForm})


def buscarEspecie(request):
    return render(request, "aplicacion/searchSpecies")
    

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        plantas = Plantas.objects.filter(especie_icontains=patron)
        contexto = {"plantas": plantas}
        return render(request, "aplicacion/plants.html", contexto)

    return HttpResponse("No se ingreso nada al buscar")











def macetas(request):
    contexto = {'flowerpot':Macetas.objects.all(), "Titel": "disponible", "descuento": ["4 por 3", "20% pagando en efectivo"]}      #Plantas' es el modelo, dice que me devuelva todos los objetos de la clase o modelo Plantas
    return render(request, "aplicacion/flowerpot.html", contexto)
    

def jardineria(request):
    contexto = {'gardering':Jardineria.objects.all(), "Titel": "disponible", "descuento": ["4 por 3", "20% pagando en efectivo"]}      #Plantas' es el modelo, dice que me devuelva todos los objetos de la clase o modelo Plantas
    return render(request, "aplicacion/gardering.html", contexto)
    

def decoracion(request):
    contexto = {'decoration':Decoracion.objects.all(), "Titel": "disponible", "descuento": ["4 por 3", "20% pagando en efectivo"]}      #Plantas' es el modelo, dice que me devuelva todos los objetos de la clase o modelo Plantas
    return render(request, "aplicacion/decoration.html", contexto)

def contacto(request):
    return render(request, "aplicacion/contact.html")

