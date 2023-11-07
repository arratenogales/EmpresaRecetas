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
    ingredientes = models.ManyToManyField(Ingrediente) #muchos ingredientes
    nombre = models.CharField(max_length=70)
    duracion = models.IntegerField()
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    def __str__(self):
        return self.nombre
