from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Recetas")
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Receta, TipoPlato, Ingrediente

#devuelve recetas por cada tipo y en orden de duracion
def index_portada(request):
    recetas = Receta.objects.values('tipoplato').order_by('duracion')
    context = {'lista_recetas_portada': recetas}
    return render(request, 'portada.html', context)

#devuelve el listado de recetas
def index_recetas(request):
	recetas = get_list_or_404(Receta.objects.order_by('nombre'))
	"""output = ', '.join([d.nombre for d in recetas])"""
	context = {'lista_recetas': recetas }
	"""return HttpResponse(output)"""
	return render(request, 'index.html', context)

def index_ingredientes(request):
	ingredientes = get_list_or_404(Ingrediente.objects.order_by('nombre'))
	"""output = ', '.join([d.nombre for i in ingredientes])"""
	context = {'lista_ingredientes': ingredientes }
	"""return HttpResponse(output)"""
	return render(request, 'ingredientes.html', context)

def index_tipos(request):
	tipos = get_list_or_404(TipoPlato.objects.order_by('nombre'))
	"""output = ', '.join([d.nombre for t in tipos])"""
	context = {'lista_tipos': tipos }
	"""return HttpResponse(output)"""
	return render(request, 'tipos.html', context)

#devuelve los datos de una receta
def show_receta(request, receta_id):
	receta = get_list_or_404(Receta.objects.get(pk=receta_id))
	"""output = f'Detalles de la receta: {receta.id},{receta.nombre}, {receta.ingredientes}, {receta.duracion}, {receta.tipo}'"""
	"""return HttpResponse(output)"""
	context = {'receta': receta }
	return render(request, 'receta.html', context)

#devuelve los detalles de un ingrediente
def show_ingrediente(request, ingrediente_id):
	ingrediente = get_list_or_404(Ingrediente.objects.get(pk=ingrediente_id))
	recetas =  ingrediente.recetas_set.all()
	context = { 'ingrediente': ingrediente, 'recetas' : recetas }
	return render(request, 'ingrediente.html', context) 
"""	output = f'Detalles del ingrediente: {ingrediente.id}, {ingrediente.nombre}, {ingrediente.kcal}, {ingrediente.grasas}'"""
"""return HttpResponse(output)"""

#devuelve los detalles de un tipo 
def show_tipo(request, tipo_id):
	tipo = get_list_or_404(TipoPlato.objects.get(pk=tipo_id))
	recetas =  tipo.recetas_set.all()
	context = { 'recetas': recetas, 'tipo' : tipo }
	return render(request, 'tipo.html', context)  
"""	output = f'Detalles de un tipo: {tipo.id}, {tipo.nombre}. Recetas: {[e.nombre for e in Receta.receta_set.all()]}'"""
"""return HttpResponse(output)"""


#nose...

#devuelve los ingredientes de una receta
def index_ingredientes_r(request, receta_id):
	receta = get_list_or_404(Receta.objects.get(pk=receta_id))
	ingredientes =  receta.ingrediente_set.all()
	"""output = ', '.join([e.nombre for e in receta.ingredientes_set.all()])"""
	"""return HttpResponse(output)"""
	context = {'receta': receta, 'ingredientes' : ingredientes }
	return render(request, 'ingredientes_r.html', context)

#devuelve las recetas de un tipo
def index_recetas_t(request, tipo_id):
	tipo = get_list_or_404(TipoPlato.objects.get(pk=tipo_id))
	recetas =  tipo.receta_set.all()
	"""output = ', '.join([e.nombre for e in tipo.recetas_set.all()])"""
	"""return HttpResponse(output)"""
	context = {'tipo': tipo, 'recetas' : recetas }
	return render(request, 'recetas_t.html', context)

#devuelve las recetas de un ingrediente
def index_recetas_i(request, ingrediente_id):
	ingrediente = get_list_or_404(Ingrediente.objects.get(pk=ingrediente_id))
	recetas =  ingrediente.receta_set.all()
	"""output = ', '.join([e.nombre for e in ingrediente.receta_set.all()])"""
	"""return HttpResponse(output)"""
	context = {'ingrediente': ingrediente, 'recetas' : recetas }
	return render(request, 'recetas_i.html', context)

