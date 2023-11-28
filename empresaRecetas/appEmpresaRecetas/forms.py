from django import forms

class Pregunta(forms.Form):
    pregunta = forms.CharField(label = "pregunta", max_length=300)
    email = forms.EmailField(label = "Email", required = True)
