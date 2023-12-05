from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Pregunta, Group, User, Comentario

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['nombre', 'apellido', 'email', 'nombreReceta', 'ingredientes', 'tipo', 'tiempo', 'detalle', 'accept']


class ComForm(forms.ModelForm):
    class Meta:
        model = Comentario  
        fields = ['correo','comentario']


class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'group')