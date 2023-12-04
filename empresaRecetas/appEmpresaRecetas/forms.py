from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Pregunta, Group, User

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['nombre', 'apellido', 'email', 'nombreReceta', 'ingredientes', 'tipo', 'tiempo', 'detalle', 'accept']


