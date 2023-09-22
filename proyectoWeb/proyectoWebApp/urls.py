from django.urls import path
from proyectoWebApp.views import home, contact, store, service, blog

urlpatterns = [
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('store/', store, name='store'),
    path('services/', service, name='services'),
    path('blog/', blog, name='blog'),
]
