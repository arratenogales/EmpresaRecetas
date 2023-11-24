from django.contrib import admin
from .models import Receta, Ingrediente, TipoPlato
'''from .models import Pregunta
from .models import Writer, Reader, Role





class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'pregunta')  # Campos que se ponen la lista
    search_fields  = ('pregunta',)




class BaseAdmin(admin.ModelAdmin):
    list_display = ('usuario',)  
    search_fields = ('nombre', 'apellidos')  
    '''

admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(TipoPlato)

'''

admin.site.register(Pregunta, BaseAdmin)


@admin.register(Writer)
class EditorAdmin(BaseAdmin):
    pass

@admin.register(Reader)
class ReaderAdmin(BaseAdmin):
    pass

admin.site.register(Role)'''
