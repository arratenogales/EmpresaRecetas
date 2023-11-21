from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(label = "nombre", max_length=100)
    apellidos = forms.CharField(label = "Apellidos", max_length=150)
    email = forms.EmailField(label = "Email", required = False)
    direccion = forms.CharField(label = "Direccion")
    edad = forms.IntegerField(label = "Edad")