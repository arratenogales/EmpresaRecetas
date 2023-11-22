from django.urls import path
from . import views

urlpatterns = [


    path('', views.index_portada, name='portada'),

    path('receta/', views.index_recetas, name='index_recetas'),
    path('ingrediente/', views.index_ingredientes, name='index_ingrediente'),
    path('tipo/', views.index_tipos, name='index_tipo'),

    path('receta/<int:receta_id>/', views.show_receta, name='receta'),
    path('ingrediente/<int:ingrediente_id>/', views.show_ingrediente, name='ingrediente'),
    path('tipo/<int:tipo_id>/', views.show_tipo, name='tipo'),
  
    path('registrar/', views.show_formulario, name='registrar'),
    path('usuario/', views.post_usuario_form, name='post_usuario_form')
]