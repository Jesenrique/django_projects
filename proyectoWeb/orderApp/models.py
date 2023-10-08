from django.db import models
#esta funcion devuelve el usuario actual, el usuario logueado
from django.contrib.auth import get_user_model

from storeApp.models import product
from django.db.models import F, Sum, FloatField

#Almacena el usuario activo
User=get_user_model()

# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    #Esta clase modifica propiedades a crearse en la tabla de la BD
    class Meta:
        db_table='order'
        verbose_name='order'
        verbose_name_plural='orders'
        ordering=['id']
    
    def __str__(self) -> str:
        return self.id
    
    @property
    def total(self):
        return self.lineorder_set.aggregate(
            total=sum(F("price")*F("quantity"), output_field=FloatField())
        )["total"]


class TableOrder(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity=models.ImageField(default=1)
    created=models.DateTimeField(auto_now_add=True)

    #Esta clase modifica propiedades a crearse en la tabla de la BD
    class Meta:
        db_table='lineorder'
        verbose_name='line order'
        verbose_name_plural='lines orders'
        ordering=['id']

    def __str__(self):
        return f'{self.id} unidades de {self.product_id.name}'
    