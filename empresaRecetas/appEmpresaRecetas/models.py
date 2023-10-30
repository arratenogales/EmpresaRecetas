from django.db import models
 
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    

class TipoPlato(models.Model):
    nombre = models.CharField(max_length=50)
 
class Receta(models.Model):
    tipo = models.ForeignKey(TipoPlato, on_delete=models.CASCADE)
    #una receta tiene varios ingredientes)
    ingredientes = models.ManyToManyField(Ingrediente)
    nombre = models.CharField(max_length=40)
    duracion = models.IntegerField()
