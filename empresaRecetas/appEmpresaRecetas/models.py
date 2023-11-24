from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    kcal = models.FloatField(default=0)
    grasas= models.FloatField(default= 0)
    def __str__(self):
        return self.nombre
    

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

class User(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    edad = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    
'''

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
    list_display = ('first_name', 'last_name', 'colored_name')'''