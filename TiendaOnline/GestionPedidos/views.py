from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Article
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import FormularioContacto


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
    if request.method == "POST":
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            info_form=miFormulario.cleaned_data
            send_mail(info_form['subject'], info_form['message'], 
                      info_form.get('email',''), ["jesus.universidad.ia@gmail.com"],)
            return render(request,"gracias.html")
        
    # si no es un  metodo post crea el formulario y se renderiza 
    else:
        miFormulario=FormularioContacto()
    
    ctx={"form":miFormulario}
    return render(request,"contacto_1.html", ctx)
        

'''
def contacto(request):
    if request.method == "POST":
        subject= request.POST["asunto"]
        email=request.POST["email"]
        message=request.POST["message"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["jesus.universidad.ia@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"gracias.html")

    return render(request,"contacto.html")
'''