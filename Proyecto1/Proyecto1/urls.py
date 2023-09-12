"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo,get_time, age_estimate

urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/",saludo),
    path("time/",get_time),
    # ver como en el path se establece un valor, ademas de ellos se tipa la 
    # variable de entrada segun la necesidad y funcionalidad de esta variable
    # con solo poner/<int:year>
    path("age_estimated/<int:year_future>/<int:year_actual>", age_estimate)
]
