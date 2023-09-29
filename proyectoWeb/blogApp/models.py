from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categorie(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #usadas para tener como referencia cuando fue creada
    updated=models.DateTimeField(auto_now_add=True) #usada como referencia para saber ultima actualizacion 
                                                    #se usa el campo auto para que se añada automaticamente
    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"
    
    def __str__(self):
        return self.name
    
class post(models.Model):
    title=models.CharField(max_length=50)  #
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='blog', null=True, blank=True) # con esto le digo que es opcional si entra o no imagen
    
    # se usa para cuando un autor se elimina tambien se borren todos los post que hizo
    autor=models.ForeignKey(User, on_delete=models.CASCADE)

    # se usa para establecer la relacion de muchos a muchos con categoria
    # un post puede estar en varias categorias y una categoria puede estar en varios post
    categories=models.ManyToManyField(categorie)
    
    created=models.DateTimeField(auto_now_add=True) #usadas para tener como referencia cuando fue creada
    updated=models.DateTimeField(auto_now_add=True) #usada como referencia para saber ultima actualizacion 
                                                    #se usa el campo auto para que se añada automaticamente
    class Meta:
        verbose_name="post"
        verbose_name_plural="posts"
    
    def __str__(self):
        return self.title