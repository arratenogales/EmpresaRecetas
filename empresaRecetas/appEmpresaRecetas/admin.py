from django.contrib import admin
from .models import Receta, Ingrediente, TipoPlato
from .models import Pregunta


admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(TipoPlato)

class PreguntaAdmin(admin.ModelAdmin):
    fields = ['fecha', 'pregunta']

admin.site.register(Pregunta, PreguntaAdmin)