from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Receta, TipoPlato, Ingrediente
from django.db.models import Max
def index(request):
    return HttpResponse("Recetas")

"""recetas_con_max_duracion =get_list_or_404(Receta.objects.order_by('duracion'))"""
   
#devuelve recetas por cada tipo y en orden de duracion
#def index_portada(request):
#    recetas_con_max_duracion =get_list_or_404( Receta.objects.values('tipo').annotate(max_duracion=Max('duracion')))
#    context = {'lista_recetas_portada': recetas_con_max_duracion}
#    return render(request, 'portada.html', context)

def index_portada(request):
    tipos_recetas = TipoPlato.objects.all()  # Obtener todos los tipos de recetas
    recetas_con_max_duracion = []

    for tipo in tipos_recetas:
        receta_max_duracion = Receta.objects.filter(tipo=tipo).order_by('-duracion').first()
        if receta_max_duracion:
            recetas_con_max_duracion.append(receta_max_duracion)

    context = {'lista_recetas_portada': recetas_con_max_duracion}
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
	receta = get_object_or_404(Receta, pk=receta_id)
	ingredientes = receta.ingredientes.all()
	"""output = f'Detalles de la receta: {receta.id},{receta.nombre}, {receta.ingredientes}, {receta.duracion}, {receta.tipo}'"""
	"""return HttpResponse(output)"""
	context = {'receta': receta, 'ingredientes': ingredientes }
	return render(request, 'receta.html', context)

#devuelve los detalles de un ingrediente 
def show_ingrediente(request, ingrediente_id):
	ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_id)
	recetas =  Receta.objects.filter(ingredientes=ingrediente)
	context = { 'ingrediente': ingrediente, 'recetas' : recetas }
	return render(request, 'ingrediente.html', context) 
"""	output = f'Detalles del ingrediente: {ingrediente.id}, {ingrediente.nombre}, {ingrediente.kcal}, {ingrediente.grasas}'"""
"""return HttpResponse(output)"""

#devuelve los detalles de un tipo 
def show_tipo(request, tipo_id):
	tipo = get_object_or_404(TipoPlato, pk=tipo_id)
	recetas =  Receta.objects.filter(tipo=tipo)
	context = { 'recetas': recetas, 'tipo' : tipo }
	return render(request, 'tipo.html', context)  
"""	output = f'Detalles de un tipo: {tipo.id}, {tipo.nombre}. Recetas: {[e.nombre for e in Receta.receta_set.all()]}'"""
"""return HttpResponse(output)"""



