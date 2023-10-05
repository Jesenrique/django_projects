from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages

#Se trabaja con una clase que ya maneja directamente la creacion de 
#nuevos usuarios

class UserRegister(View):

    def get(self,request):
        form=UserCreationForm()
        return render(request, "auth.html",{"form":form})
    
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
            return render(request, "auth.html",{"form":form})
        
def CloseSession(request):
    logout(request)
    return redirect('home')

def UserLogin(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            USERNAME=form.cleaned_data.get("username")
            PASSWORD=form.cleaned_data.get("password")
            user=authenticate(username=USERNAME,password=PASSWORD)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"usuario no valido!")
        else:
            messages.error(request,"Información incorrecta")
            
    form=AuthenticationForm()
    return render(request,'login.html',{"form":form})