from django.urls import path
from authentification import views

urlpatterns = [
    path('', views.UserRegister.as_view(), name='login'),
    path('close_session', views.CloseSession, name='close_session'),
]
