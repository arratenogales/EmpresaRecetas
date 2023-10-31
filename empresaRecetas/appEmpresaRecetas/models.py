from django.db import models
 
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
    #una receta tiene varios ingredientes)
    ingredientes = models.ManyToManyField(Ingrediente)
    nombre = models.CharField(max_length=40)
    duracion = models.IntegerField()
    def __str__(self):
        return self.nombre
