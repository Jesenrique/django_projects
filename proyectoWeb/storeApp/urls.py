from django.urls import path
from storeApp.views import store

urlpatterns = [
    path('', store, name='store'),
]
