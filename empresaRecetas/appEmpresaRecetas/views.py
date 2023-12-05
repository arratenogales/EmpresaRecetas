from django.shortcuts import render, redirect,  get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Receta, TipoPlato, Ingrediente, Comentario
from .forms import RecetaForm, ComForm
from django.views.generic import ListView, DetailView,View,TemplateView

#from django.contrib.contenttypes.models import ContentType


def index(request):
    return HttpResponse("Recetas")

#vista de la portada en la que se muetsran las 4 recetas 1 de cada tipo con menor duracion. 
class IndexPortadaView(TemplateView):
    template_name = 'portada.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recetas_con_max_duracion = Receta.objects.raw('''
            SELECT * FROM appEmpresaRecetas_Receta
            WHERE (tipo_id, duracion) IN (
                SELECT tipo_id, MIN(duracion) as max_duracion
                FROM appEmpresaRecetas_Receta
                GROUP BY tipo_id
            )
        ''')
        context['lista_recetas_portada'] = recetas_con_max_duracion
        return context

def index_portada(request):
    recetas_con_max_duracion =  Receta.objects.raw('SELECT * FROM appEmpresaRecetas_Receta WHERE (tipo_id, duracion) IN ( SELECT tipo_id, MIN(duracion) as max_duracion FROM appEmpresaRecetas_Receta GROUP BY tipo_id)')
    context = {'lista_recetas_portada': recetas_con_max_duracion}
    return render(request, 'portada.html', context)


# Vista basada en clases en todas las funcionalidades básicas (listado de las recetas).
class IndexRecetasListView(ListView):
    model = Receta
    template_name = 'index.html'
    queryset = Receta.objects.order_by('nombre')
    context_object_name = 'lista_recetas'

    def get_context_data(self, **kwargs):
        context = super(IndexRecetasListView, self).get_context_data(**kwargs)
        context['titulo de la pagina'] = 'Listado de recetas'
        return context

def index_recetas(request):
	recetas = get_list_or_404(Receta.objects.order_by('nombre'))
	"""output = ', '.join([d.nombre for d in recetas])"""
	context = {'lista_recetas': recetas }
	"""return HttpResponse(output)"""
	return render(request, 'index.html', context)




# Vista basada en clases en todas las funcionalidades básicas (listado de los ingredientes).

class IndexIngredientesListView(ListView):
    model = Ingrediente
    template_name = 'ingredientes.html'
    queryset = Receta.objects.order_by('nombre')
    context_object_name = 'lista_ingredientes'

    def get_context_data(self, **kwargs):
        context = super(IndexIngredientesListView, self).get_context_data(**kwargs)
        context['titulo de la pagina'] = 'Listado de ingredientes'
        return context

def index_ingredientes(request):
	ingredientes = get_list_or_404(Ingrediente.objects.order_by('nombre'))
	"""output = ', '.join([d.nombre for i in ingredientes])"""
	context = {'lista_ingredientes': ingredientes }
	"""return HttpResponse(output)"""
	return render(request, 'ingredientes.html', context)
from django.http import JsonResponse




# Vista basada en clases en todas las funcionalidades básicas (listado de los tipos).

class IndexTiposListView(ListView):
    model = TipoPlato
    template_name = 'tipos.html'
    queryset = Receta.objects.order_by('nombre')
    context_object_name = 'lista_tipos'

    def get_context_data(self, **kwargs):
        context = super(IndexTiposListView, self).get_context_data(**kwargs)
        context['titulo de la pagina'] = 'Listado de tipos'
        return context

def index_tipos(request):
	tipos = get_list_or_404(TipoPlato.objects.order_by('nombre'))
	"""output = ', '.join([d.nombre for t in tipos])"""
	context = {'lista_tipos': tipos }
	"""return HttpResponse(output)"""
	return render(request, 'tipos.html', context)



# Vista basada en clases en todas las funcionalidades básicas (detalles de una receta).

class RecetaDetailView(DetailView):
     model = Receta
     template_name= 'receta.html'

     def get_context_data(self, **kwargs):
        context = super(RecetaDetailView, self).get_context_data(**kwargs)
        context['titulo de la pagina'] = 'Detalles de la receta'
        return context
     
def show_receta(request, receta_id):
	receta = get_object_or_404(Receta, pk=receta_id)
	ingredientes = receta.ingredientes.all()
	"""output = f'Detalles de la receta: {receta.id},{receta.nombre}, {receta.ingredientes}, {receta.duracion}, {receta.tipo}'"""
	"""return HttpResponse(output)"""
	context = {'receta': receta, 'ingredientes': ingredientes }
	return render(request, 'receta.html', context)



# Vista basada en clases en todas las funcionalidades básicas (detalles de un ingrediente).

class ImgredienteDetailView(DetailView):
     model = Ingrediente
     template_name= 'ingrediente.html'

     def get_context_data(self, **kwargs):
        context = super(ImgredienteDetailView, self).get_context_data(**kwargs)
        context['titulo de la pagina'] = 'Detalles del ingrediente'
        return context

def show_ingrediente(request, ingrediente_id):
	ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_id)
	recetas = ingrediente.receta_set.all()
	context = { 'ingrediente': ingrediente, 'recetas' : recetas }
	return render(request, 'ingrediente.html', context) 




# Vista basada en clases en todas las funcionalidades básicas (detalles de un tipo).

class TipoDetailView(DetailView):
     model = TipoPlato
     template_name= 'tipo.html'
     def get_context_data(self, **kwargs):
        context = super(ImgredienteDetailView, self).get_context_data(**kwargs)
        context['titulo de la pagina'] = 'Detalles del tipo'
        return context
 
def show_tipo(request, tipo_id):
	tipo = get_object_or_404(TipoPlato, pk=tipo_id)
	recetas = tipo.receta_set.all()
	context = { 'recetas': recetas, 'tipo' : tipo }
	return render(request, 'tipo.html', context)  


#VISTAS BASADAS EN CLASES sobre el formulario: 


class IndexComentariosView(ListView):
    model = Comentario
    template_name= 'comentario.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comentarios = Comentario.objects.order_by('correo')
        context['comentarios'] = comentarios
        return context
    
def index_comentarios(request):
    comentarios = Comentario.objects.order_by('correo')
    context = {'comentarios': comentarios}
    return render(request, 'comentario.html', context)

#vista relacionada con el formulario de preguntas acerca de la receta. 
class ShowFormularioView(View):
    template_name = 'formulario.html'

    def get(self, request):
        formulario = RecetaForm()
        return render(request, self.template_name, {'formulario': formulario})

    def post(self, request):
        formulario = RecetaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_recetas')

        return render(request, self.template_name, {'formulario': formulario})
    
def show_formulario(request):
    if request.method == 'POST':
        formulario = RecetaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_recetas')      
    else:
        formulario = RecetaForm()

    return render(request, 'formulario.html', {'formulario': formulario})

#vistas relacionadas con el formulario de comentarios. 
class LoginFormView(View):
    template_name = 'index.html'

    def get(self, request):
        form = ComForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ComForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_recetas')
        return render(request, self.template_name, {'form': form})
    
def loginform(request):
    if request.method == 'POST':
        form = ComForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_recetas')
    else:
        form = ComForm()
    return render(request, 'index.html', {'form': form})