from django.db import models

# Create your models here.
class categorieProduct(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="categorieProduct"
        verbose_name_plural="categoriesProduct"
    
    def __str__(self) -> str:
        return self.name

class product(models.Model):
    name=models.CharField(max_length=50)
    categorie=models.ForeignKey(categorieProduct, on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True) 
    avaible=models.BooleanField(default=True)
    price=models.FloatField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="product"
        verbose_name_plural="products"
    