from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Receta, TipoPlato, Ingrediente
from django.shortcuts import redirect

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType


def index(request):
    return HttpResponse("Recetas")


from .forms import UsuarioForm

"""def show_formulario(request):
    return render(request, 'registro.html')
"""

def show_formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid() and form.cleaned_data['Accept']:
            nuevo_usuario = User(
                nombre=form.cleaned_data['nombre'],
                apellidos=form.cleaned_data['apellidos'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                direccion=form.cleaned_data['direccion'],
                usuario=form.cleaned_data['usuario'],
                contraseña=form.cleaned_data['contraseña'],
            )
            nuevo_usuario.save()

            # intento de permisos para editar recetas
            if request.user.is_authenticated: 
                content_type = ContentType.objects.get_for_model(Receta)
                add_permission = Permission.objects.get(content_type=content_type, codename='add_receta')
                change_permission = Permission.objects.get(content_type=content_type, codename='change_receta')
                delete_permission = Permission.objects.get(content_type=content_type, codename='delete_receta')
                nuevo_usuario.user_permissions.add(add_permission, change_permission, delete_permission)


            return redirect('portada')
        else:
            form.add_error('Accept', 'Debes aceptar las condiciones para registrarte.')


    else:
        form = UsuarioForm()

    return render(request, 'registro.html', {'form': form})

"""
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
	recetas = ingrediente.receta_set.all()
	context = { 'ingrediente': ingrediente, 'recetas' : recetas }
	return render(request, 'ingrediente.html', context) 
"""	output = f'Detalles del ingrediente: {ingrediente.id}, {ingrediente.nombre}, {ingrediente.kcal}, {ingrediente.grasas}'"""

#devuelve los detalles de un tipo 
def show_tipo(request, tipo_id):
	tipo = get_object_or_404(TipoPlato, pk=tipo_id)
	recetas = tipo.receta_set.all()
	context = { 'recetas': recetas, 'tipo' : tipo }
	return render(request, 'tipo.html', context)  
"""	output = f'Detalles de un tipo: {tipo.id}, {tipo.nombre}. Recetas: {[e.nombre for e in Receta.receta_set.all()]}'"""
"""return HttpResponse(output)"""


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect




from django.shortcuts import render, redirect
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