from django.shortcuts import render, redirect,  get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Receta, TipoPlato, Ingrediente, Pregunta
from django.views.generic import ListView, DetailView

#from django.contrib.contenttypes.models import ContentType


def index(request):
    return HttpResponse("Recetas")

"""
def show_formulario(request):
    return render(request, 'formulario.html')

"""
def show_formulario(request):
    if request.method == 'POST':
        formulario = Pregunta(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('formulario') 
    else:
        formulario = Pregunta()

    return render(request, 'formulario.html', {'formulario': formulario})

"""
def show_formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid() and form.cleaned_data['Accept']:

            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Este correo electrónico ya está registrado.')
                return render(request, 'registro.html', {'form': form})

            nuevo_usuario = User.objects.create_user(
                nombre=form.cleaned_data['nombre'],
                apellidos=form.cleaned_data['apellidos'],
                email=email,
                edad=form.cleaned_data['edad'],
                direccion=form.cleaned_data['direccion'],
                username=form.cleaned_data['username'],
            )
            nuevo_usuario.set_password(form.cleaned_data['password'])
            nuevo_usuario.save()

            # intento de permisos para editar recetas (management/commands/permissions.py)
            if request.user.is_authenticated and isinstance(nuevo_usuario, User):
                content_type = ContentType.objects.get_for_model(Receta)
                add_permission = Permission.objects.get(content_type=content_type, codename='add_receta')
                change_permission = Permission.objects.get(content_type=content_type, codename='change_receta')
                delete_permission = Permission.objects.get(content_type=content_type, codename='delete_receta')
                nuevo_usuario.user_permissions.add(add_permission, change_permission, delete_permission)


            user = authenticate(username=form.cleaned_data['usuario'], password=form.cleaned_data['contraseña'])
            login(request, user) #se supone que para que el usuario autenticado acceda a las vistas restringidas 
                        
            return redirect('portada')


        else:
            form.add_error('Accept', 'Debes aceptar las condiciones para registrarte.')


    else:
        form = UsuarioForm()

    return render(request, 'registro.html', {'form': form})


def post_usuario_form(request): 
    form = UsuarioForm(request.POST)
    if form.is_valid():
        form.save() 
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']        
        return HttpResponse(f"Registro exitoso. Bienvenid@ {nombre} {apellidos}")



"""


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
"""	output = f'Detalles del ingrediente: {ingrediente.id}, {ingrediente.nombre}, {ingrediente.kcal}, {ingrediente.grasas}'"""



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
"""	output = f'Detalles de un tipo: {tipo.id}, {tipo.nombre}. Recetas: {[e.nombre for e in Receta.receta_set.all()]}'"""
"""return HttpResponse(output)"""


"""

from django.contrib.auth import authenticate, login
from .forms import InicioSesionForm

def iniciar_sesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['contra']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                print("Usuario autenticado y sesión establecida:", user)
                # Redirigir a una página de éxito o a donde desees después del inicio de sesión
                return redirect('EmpresaRecetas:writters')
            else:
                print("Credenciales no válidas")

    else:
        form = InicioSesionForm()

    return render(request, 'login.html', {'form': form})

def show_writters(request):
    return render(request, 'writters.html')

"""