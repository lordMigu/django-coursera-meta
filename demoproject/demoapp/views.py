from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def index(request): 
    return HttpResponse("<h1>Hola mundo!. Este es un view de index de Permatrago, Exprimo, Crotolamo, Obo y demas cosas.</h1>")

def paramRuta(request, nombre, apellido, id):
    return HttpResponse(f"Nombre: {nombre} Apellido: {apellido} ID: {id}")

def paramConsulta(request):
    base = int(request.GET['base'])
    potencia = int(request.GET['potencia'])
    return HttpResponse(f'La potencia {potencia} de {base} es: {base**potencia}')

def showform(request): 
    return render(request, "form.html")

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))