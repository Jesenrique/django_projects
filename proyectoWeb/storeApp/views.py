from django.shortcuts import render
from .models import categorieProduct, product

# Create your views here.
def store(request):
    products=product.objects.all()
    return render(request, "storeApp/store.html", {"products":products})

