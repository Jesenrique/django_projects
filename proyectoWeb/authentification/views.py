from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


#Se trabaja con una clase que ya maneja directamente la creacion de 
#nuevos usuarios

class UserRegister(View):

    def get(self,request):
        form=UserCreationForm()
        return render(request, "login.html",{"form":form})
    
    def post(self,request):
        form=UserCreationForm(request.POST)
        user=form.save()
        login(request,user)

        return redirect(request, "login.html",{"form":form})