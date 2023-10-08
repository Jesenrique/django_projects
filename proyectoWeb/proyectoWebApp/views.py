from django.shortcuts import render
from django.http import HttpResponse, request

from carApp.car import Car

# Create your views here.

def home(request):
    #Es importante instanciar el objeto carro apenas se inicie la vista home
    # para evitar errores
    car=Car(request) 
    return render(request, "proyectoWebApp/home.html")
