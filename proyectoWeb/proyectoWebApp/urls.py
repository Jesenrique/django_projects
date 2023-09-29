from django.urls import path
from proyectoWebApp.views import home

urlpatterns = [
    path('home/', home, name='home'),
]
