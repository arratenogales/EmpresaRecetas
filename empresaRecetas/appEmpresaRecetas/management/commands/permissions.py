
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from appEmpresaRecetas.models import Receta

class Command(BaseCommand):
    help = 'Crea los permisos necesarios para el modelo Receta'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Receta)

        add_perm = Permission.objects.create(
            codename='add_receta',
            name='Can add receta',
            content_type=content_type,
        )

        change_perm = Permission.objects.create(
            codename='change_receta',
            name='Can change receta',
            content_type=content_type,
        )

        delete_perm = Permission.objects.create(
            codename='delete_receta',
            name='Can delete receta',
            content_type=content_type,
        )

        self.stdout.write(self.style.SUCCESS('Permisos creados con éxito.'))
