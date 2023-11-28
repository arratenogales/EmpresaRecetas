from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .models import UserProfile
from django.contrib.auth.models import Group, Permission, User
from django.utils.translation import gettext_lazy as _
from .models import Receta, Ingrediente, TipoPlato, Pregunta


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'nombre', 'apellido', 'get_role_display')

    def nombre(self, obj):
        return obj.nombre
    nombre.short_description = _('Nombre')

    def apellido(self, obj):
        return obj.apellido
    apellido.short_description = _('Apellido')

    def get_role_display(self, obj):
        return obj.role
    get_role_display.short_description = _('Role')

# Registrar el modelo de usuario por defecto y la clase de administración
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# Crear grupos y asignar permisos
#admin_group, created = Group.objects.get_or_create(name='Administradores')
#editor_group, created = Group.objects.get_or_create(name='Editores')


# Asignar permisos a los grupos
# Ejemplo: Asignar permiso para cambiar usuarios
#admin_group.permissions.add(
#    Permission.objects.get(codename='change_user')
#)



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
admin.site.register(Pregunta)

'''

admin.site.register(Pregunta, BaseAdmin)


@admin.register(Writer)
class EditorAdmin(BaseAdmin):
    pass

@admin.register(Reader)
class ReaderAdmin(BaseAdmin):
    pass

admin.site.register(Role)'''
