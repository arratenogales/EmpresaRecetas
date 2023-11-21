from django.contrib import admin
from .models import Receta, Ingrediente, TipoPlato
from .models import Pregunta, Author
from .models import Author, Editor, Reader


admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(TipoPlato)


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'pregunta')  # Campos a mostrar en la lista
    search_fields  = ('pregunta',)

admin.site.register(Pregunta, PreguntaAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nac', 'pais') 
    search_fields  = ('nombre', 'pais')  

admin.site.register(Author, AuthorAdmin)


@admin.register(Editor, Reader)
class PersonAdmin(admin.ModelAdmin):
    pass