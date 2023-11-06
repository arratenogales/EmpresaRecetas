from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Recetas")

from django.http import HttpResponse
from .models import Receta, TipoPlato, Ingrediente

#devuelve el listado de recetas
def index_recetas(request):
	recetas = Receta.objects.order_by('nombre')
	output = ', '.join([d.nombre for d in recetas])
	return HttpResponse(output)

#devuelve los datos de una receta
def show_receta(request, receta_id):
	receta = Receta.objects.get(pk=receta_id)
	output = f'Detalles de la receta: {receta.id},{receta.nombre}, {receta.ingredientes}, {receta.duracion}, {receta.tipo}'
	return HttpResponse(output)

#devuelve los ingredientes de una receta
def index_ingredientes(request, receta_id):
	receta = Receta.objects.get(pk=receta_id)
	output = ', '.join([e.nombre for e in receta.ingredientes_set.all()])
	return HttpResponse(output)

#devuelve los detalles de un ingrediente 
def show_ingrediente(request, ingrediente_id):
	ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
	output = f'Detalles del ingrediente: {ingrediente.id}, {ingrediente.nombre}, {ingrediente.kcal}, {ingrediente.grasas}'
	return HttpResponse(output)

#devuelve los detalles de un tipo 
def show_tipo(request, tipo_id):
	tipo = TipoPlato.objects.get(pk=tipo_id)
	output = f'Detalles de un tipo: {tipo.id}, {tipo.nombre}. Recetas: {[e.nombre for e in Receta.receta_set.all()]}'
	return HttpResponse(output)
