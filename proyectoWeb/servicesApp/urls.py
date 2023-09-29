from django.urls import path
from servicesApp.views import service

urlpatterns = [
    path('', service, name='services'), # se deja sin dirección ya que ya apunta directamente a esta dirección
]
