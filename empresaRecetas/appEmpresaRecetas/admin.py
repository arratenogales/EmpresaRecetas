from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Receta, Ingrediente, TipoPlato
admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(TipoPlato)