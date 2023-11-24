from django import forms


class UsuarioForm(forms.Form):
    nombre = forms.CharField(label = "nombre", max_length=100)
    apellidos = forms.CharField(label = "Apellidos", max_length=150)
    email = forms.EmailField(label = "Email", required = False)
    direccion = forms.CharField(label = "Direccion")
    edad = forms.IntegerField(label="Edad") 
    usuario = forms.CharField(label="Usuario", max_length=150)
    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class InicioSesionForm(forms.Form):
    usuario = forms.CharField(label='Usuario')
    contra = forms.CharField(label='Contraseña', widget=forms.PasswordInput) 