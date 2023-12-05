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
        return f"{self.correo} - {self.comentario}"
    
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
    video = models.URLField(blank=True, null=True)

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

    def __str__(self):
        return f'{self.nombreReceta} - {self.nombre} {self.apellido}'

