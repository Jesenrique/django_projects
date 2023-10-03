"""proyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings # es importante importar para usar las direcciones de MEDIA
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('proyectoWebApp.urls')),
    path('services/',include('servicesApp.urls')),
    path('blog/',include('blogApp.urls')),
    path('contact/',include('contactoApp.urls')),
    path('store/',include('storeApp.urls')),
    path('car/',include('carApp.urls')),
    path('login/',include('authentification.urls')),
]

# se agrega a url patterns la url de los archivos estaticos
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)