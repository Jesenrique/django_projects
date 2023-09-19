from django.db import models

# Create your models here.
class Clientes(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)


class Article(models.Model):
    name=models.CharField(max_length=30, verbose_name="Nombre")
    section=models.CharField(max_length=20)
    price=models.IntegerField()
    
    def iva(self):
        return print(f"El iva del producto es {self.price*0.19}")

    #def __str__(self) -> str:
    #    return self.name

class Order(models.Model):
    number=models.IntegerField()
    date=models.DateField()
    status=models.BooleanField()