from django import forms

from .models import Pregunta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['nombre', 'apellido', 'email', 'nombreReceta', 'ingredientes', 'tipo', 'tiempo', 'detalle', 'accept']

