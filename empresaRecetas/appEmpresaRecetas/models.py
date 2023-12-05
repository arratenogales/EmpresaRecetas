from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    kcal = models.FloatField(default=0)
    grasas= models.FloatField(default= 0)
    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    correo = models.EmailField()
    comentario = models.CharField(max_length=500)
    def __str__(self):
        return self.correo
    
class TipoPlato(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
 
class Receta(models.Model):
    tipo = models.ForeignKey(TipoPlato, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente) #muchos ingredientes
    nombre = models.CharField(max_length=70)
    duracion = models.IntegerField()
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    nombre = models.CharField(max_length=100, default='')
    apellido = models.CharField(max_length=100, default='')
    email = models.EmailField()
    
    nombreReceta = models.CharField(max_length=100, default='')
    ingredientes= models.CharField(max_length=500, default='')
    TIPO_CHOICES = [
        ('Entrante', 'Entrante'),
        ('Primero', 'Primero'),
        ('Segundo', 'Segundo'),
        ('Postre', 'Postre'),
    ]
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES, default='')
    tiempo = models.IntegerField( default=0)


    detalle = models.TextField(default='')
    accept = models.BooleanField(default= False)

    def __str__(self):
        return f'{self.nombreReceta} - {self.nombre} {self.apellido}'


'''
class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=50 )
    apellido = models.CharField(max_length=50 )
    usuario = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('user', 'Usuario'),
    )
    #role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='customuser_set')
'''

'''
@receiver(post_save, sender=User)
def assign_reader_group(sender, instance, created, **kwargs):
    if created:
        # Define los roles y permisos correspondientes
        reader_permissions = [
            'view_receta',
            'view_ingrediente',
            'view_tipo_plato',
        ]

        # Asigna el usuario al grupo correspondiente
        reader_group, created = Group.objects.get_or_create(name='ReadersRecetas')
        instance.groups.add(reader_group)

        # Asigna permisos al usuario
        for permission_codename in reader_permissions:
            permission = Permission.objects.get(codename=permission_codename)
            instance.user_permissions.add(permission)
'''

'''
class UserProfile(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50 )
    apellido = models.CharField(max_length=50 )
    usuario = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=(
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('user', 'Usuario'),
    ), default='user')

    def __str__(self):
        return self.user.username
'''
"""   
class User(AbstractUser):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=40)
    username = models.CharField(unique=True, max_length=20)
    role = models.CharField(max_length=20, default='user')
  #  password = models.CharField(max_length=255)
    REQUIRED_FIELDS = ['email']
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('visitor', 'Visitor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


    def __str__(self):
        return self.username



admin_group = Group.objects.create(name='Administradores')
editor_group = Group.objects.create(name='Editores')
admin_group.permissions.add(Permission.objects.get(codename='add_custommodel'))
editor_group.permissions.add(Permission.objects.get(codename='change_custommodel'))




from django.contrib.auth.models import Group, Permission
from django.contrib import admin
from django.utils.html import format_html
  class Pregunta(models.Model):
    fecha = models.DateTimeField('Fecha de publicación')
    pregunta = models.CharField(max_length=200)

    def __str__(self):
        return self.pregunta 


#roles
class Role(models.Model):
    name = models.CharField(max_length=205, unique=True)

    def __str__(self):
        return self.name


wr_group, creado = Group.objects.get_or_create(name='Writer')
if creado:
    wr_group.permissions.add(
        Permission.objects.get(codename='view_receta'),
        Permission.objects.get(codename='add_receta'),
        Permission.objects.get(codename='change_receta'),
        Permission.objects.get(codename='delete_receta'),
    )

rd_group, creado = Group.objects.get_or_create(name='Reader')
if creado:
    rd_group.permissions.add(
        Permission.objects.get(codename='view_receta'),
    )

    
class Reader(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Writer(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    edad = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario
    

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=6)

    @admin.display
    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.color_code,
            self.first_name,
            self.last_name,
        )

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'colored_name')

"""    