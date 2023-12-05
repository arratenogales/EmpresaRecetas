from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
#from .models import UserProfile
from django.contrib.auth.models import Group, Permission, User
from django.utils.translation import gettext_lazy as _
from .models import Receta, Ingrediente, TipoPlato, Pregunta,Comentario
from .forms import CustomUserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver


'''
class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('group',)



class CustomUserChangeForm(UserChangeForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields + ('group',)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role_display')

    def get_role_display(self, obj):
        groups = ', '.join([group.name for group in obj.groups.all()])
        return groups
    get_role_display.short_description = _('Groups')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

'''


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('group',)}),
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)


# Crear grupos y asignar permisos
admin_group, created = Group.objects.get_or_create(name='AdminsRecetas')
reader_group, created = Group.objects.get_or_create(name='ReadersRecetas')

change_receta_permission = Permission.objects.get(codename='change_receta')
add_receta_permission = Permission.objects.get(codename= "add_receta")
change_ingrediente_permission = Permission.objects.get(codename='change_ingrediente')
add_ingrediente_permission = Permission.objects.get(codename= "add_ingrediente")
change_tipo_plato_permission = Permission.objects.get(codename='change_tipoplato')
add_tipo_plato_permission = Permission.objects.get(codename= "add_tipoplato")
add_group_permission = Permission.objects.get(codename= "add_group")
change_group_permission = Permission.objects.get(codename= "change_group")
add_permission_permission = Permission.objects.get(codename= "add_permission")
change_permission_permission = Permission.objects.get(codename= "change_permission")
add_user_peremission = Permission.objects.get(codename = "add_user")
change_user_permission = Permission.objects.get(codename = "change_user")

view_receta_permission = Permission.objects.get(codename='view_receta')
view_ingrediente_permission = Permission.objects.get(codename='view_ingrediente')
view_tipo_plato_permission = Permission.objects.get(codename='view_tipoplato')

admin_group.permissions.add(change_receta_permission, change_ingrediente_permission, change_tipo_plato_permission, add_receta_permission,
                            add_ingrediente_permission, add_tipo_plato_permission, add_group_permission, change_group_permission, add_permission_permission,
                            change_permission_permission, add_user_peremission, change_user_permission
                              )
reader_group.permissions.add(view_receta_permission, view_ingrediente_permission, view_tipo_plato_permission)




'''from .models import Pregunta
from .models import Writer, Reader, Role

##hola es una prueba



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
admin.site.register(Comentario)
'''

admin.site.register(Pregunta, BaseAdmin)


@admin.register(Writer)
class EditorAdmin(BaseAdmin):
    pass

@admin.register(Reader)
class ReaderAdmin(BaseAdmin):
    pass

admin.site.register(Role)'''