from django.shortcuts import render, redirect
from contactoApp.forms import contactForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage


# Create your views here.
def contact(request):
    dataContactForm=contactForm()
    if request.method=="POST":
        dataContactForm=contactForm(data=request.POST)
        if dataContactForm.is_valid():
            '''
            #primera forma de enviar correo, usando el send_mail se necesita importar 

            dataCleanCotactForm=dataContactForm.cleaned_data
            send_mail(dataCleanCotactForm['subject'], dataCleanCotactForm['content'],
                       settings.EMAIL_HOST_USER, ["jesus.universidad.ia@gmail.com"],)
            
            '''

            #Segunda forma de envio mediante email usando emailmessage
            name=request.POST.get('name')
            email=request.POST.get('mail')
            subject=request.POST.get('subject')
            content=request.POST.get('content')

            email=EmailMessage("Mesanje desde AppDjango",
                               f"Hola! el usuario {name} con dirección de email {email}, ha escrito lo siguiente: \n{content}", 
                               settings.EMAIL_HOST_USER, ["jesus.universidad.ia@gmail.com"] )
            
            #Este codigo me permite identificar si se entra a la pagina por 
            #primera vez o se esta enviando un formulario, se redirecciona a 
            #esa url y se valida en el html si tiene valid o no
            try:
                email.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?invalid")
            

            


    return render(request, "contact/contact.html",{"ContactForm":dataContactForm})
