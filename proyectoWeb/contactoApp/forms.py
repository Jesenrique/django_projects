from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100, required=True)
    subject = forms.CharField(label="Asunto", max_length=100, required=True)
    mail = forms.EmailField(label="E-mail", max_length=100, required=True)
    content=forms.CharField(label="Contenido", widget=forms.Textarea, max_length=500, required=True)
