from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from .models import User
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

'''
class MyAdminSite(admin.AdminSite):
    site_header = "Recetas application administration"

admin_site = MyAdminSite(name="admin")
'''

'''

class UserAdmin(UserAdmin):
    # Personaliza la visualización de usuarios en el panel de administración
    list_display = ('nombre', 'email', 'username', 'role')

admin.site.register(User, UserAdmin)

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
