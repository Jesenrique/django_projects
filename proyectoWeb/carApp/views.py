from django.shortcuts import render, redirect
from carApp.car import Car
from storeApp.models import product


# Create your views here.
# para trabajar en el carro traemos los productos
def agregate_product(request, product_id):
    car=Car(request)
    Product=product.objects.get(id=product_id)
    car.agregate(Product)
    return redirect("store")

def eliminate_product(request, product_id):
    car=Car(request)
    Product=product.objects.get(id=product_id)
    car.eliminate(Product)
    return redirect("store")

def substract_product(request, product_id):
    car=Car(request)
    Product=product.objects.get(id=product_id)
    car.substract_product(Product)
    return redirect("store")

def clean_car(request):
    car=Car(request)
    car.clean_car()
    return redirect("store")