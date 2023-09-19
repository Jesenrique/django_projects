from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Article

# Create your views here.

def busqueda(request):
    return render(request, "formulario.html")


def buscar(request):
    if request.GET["fname"]:
        #message="Usuario buscado: %r" %request.GET["fname"]
        producto=request.GET["fname"]
        articulos=Article.objects.filter(name__icontains=producto)
        print(articulos)
        ctx={"articulo":articulos, "query":producto}
        return render(request, "resultados.html",ctx)
    else:
        message="No se encontro nada"
        return HttpResponse(message)

def contacto(request):
    return render(request,"contacto.html")