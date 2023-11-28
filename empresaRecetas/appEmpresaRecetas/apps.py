from django.apps import AppConfig
#from django.db.models.signals import post_migrate
#from django.contrib.contenttypes.models import ContentType
#from .models import User

class AppEmpresaRecetasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appEmpresaRecetas'

    
'''
    def ready(self):
        post_migrate.connect(self.create_custom_permissions, sender=self)

    def create_custom_permissions(self, sender, **kwargs):
        # Import Permission inside the method to avoid AppRegistryNotReady
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.auth.models import Permission, Group

        content_type = ContentType.objects.get_for_model(User)

        # Crear permiso si no existe
        can_view_dashboard, created = Permission.objects.get_or_create(
            codename='can_view_dashboard',
            name='Can view dashboard',
            content_type=content_type,
        )
'''

'''
class MyAdminConfig(AdminConfig):
    default_site = 'myproject.admin.MyAdminSite'
'''