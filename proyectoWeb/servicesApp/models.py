from django.db import models

# Create your models here.
class services(models.Model):
    tittle=models.CharField(max_length=50)  #
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='services') # upload_to sirve para indicar en que carpeta de media se guardara
    # si no es pecifica se guarda en la carpeta media, la cual es la base configurada en settings
    created=models.DateTimeField(auto_now_add=True) #usadas para tener como referencia cuando fue creada
    updated=models.DateTimeField(auto_now_add=True) #usada como referencia para saber ultima actualizacion 
                                                    #se usa el campo auto para que se añada automaticamente
    class Meta:
        verbose_name="service"
        verbose_name_plural="services"
    
    def __str__(self):
        return self.tittle