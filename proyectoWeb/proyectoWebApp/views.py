from django.shortcuts import render
from django.http import HttpResponse, request
from servicesApp.models import services

# Create your views here.

def home(request):
    return render(request, "proyectoWebApp/home.html")


def service(request):
    servicio=services.objects.all()  #con esto me traigo todo los servicios del modelo
    ctx={"servicios":servicio}
    return render(request, "proyectoWebApp/services.html",ctx)


def store(request):
    return render(request, "proyectoWebApp/store.html")


def contact(request):
    return render(request, "proyectoWebApp/contact.html")


def blog(request):
    return render(request, "proyectoWebApp/blog.html")
