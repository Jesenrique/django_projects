from django.shortcuts import render
from servicesApp.models import services

# Create your views here.
def service(request):
    servicio=services.objects.all()  #con esto me traigo todo los servicios del modelo
    ctx={"servicios":servicio}
    return render(request, "services/services.html",ctx)