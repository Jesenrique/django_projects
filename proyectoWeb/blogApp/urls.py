from django.urls import path
from blogApp.views import blog, blog_categorie

urlpatterns = [
    path('', blog, name='blog'), # se deja sin dirección ya que ya apunta directamente a esta dirección
    path('categoria/<categorie_id>', blog_categorie, name='blog_categorie'),
]
