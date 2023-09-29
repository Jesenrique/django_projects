from django.urls import path
from contactoApp import views


urlpatterns = [
    path('', views.contact, name='contact'),

]
