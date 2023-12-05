from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
#from .models import UserProfile
from django.contrib.auth.models import Group, Permission, User
from django.utils.translation import gettext_lazy as _
from .models import Receta, Ingrediente, TipoPlato, Pregunta,Comentario
from .forms import CustomUserCreationForm
from django.dispatch import receiver




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





admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(TipoPlato)
admin.site.register(Pregunta)
admin.site.register(Comentario)

