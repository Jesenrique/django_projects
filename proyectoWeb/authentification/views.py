from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib import messages

#Se trabaja con una clase que ya maneja directamente la creacion de 
#nuevos usuarios

class UserRegister(View):

    def get(self,request):
        form=UserCreationForm()
        return render(request, "login.html",{"form":form})
    
    #metodo usado para guardar los datos en la base de datos
    def post(self,request):
        form=UserCreationForm(request.POST)
        #Existen una serie de pasos para registrarse y debe loguerase si el 
        #formulario no da error
        if form.is_valid():
            #almacena automaticamente los valores de los campos en la base de 
            #datos
            user=form.save()
            #Esto loguea al usuario automaticamente
            login(request,user)
            return redirect('home')
        
        #esto me servira para indicarle al template en que fallo para registrarse
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "login.html",{"form":form})
        
def CloseSession(request):
    logout(request)
    return redirect('home')