from django import forms


class FormularioContacto(forms.Form):
    name=forms.CharField(label="Cual es tu nombre...", max_length="50")
    subject=forms.CharField(label="Escribe el asunto...", max_length="100")
    email=forms.EmailField
    message=forms.CharField(label="Escribe el motivo de la solicitud...", max_length="600")
