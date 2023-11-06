from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_portada, name='portada'),

    path('receta/', views.index_recetas, name='index_receta'),
    path('ingrediente/', views.index_ingredientes, name='index_ingrediente'),
    path('tipo/', views.index_tipos, name='index_tipo'),

    path('receta/<int:receta_id>/', views.show_receta, name='receta'),
    path('ingrediente/<int:ingrediente_id>/', views.show_ingrediente, name='ingrediente'),
    path('tipo/<int:tipo_id>/', views.show_tipo, name='tipo'),
    
    #ingredientes de una receta
    path('receta/<int:receta_id>/ingredientes', views.index_ingredientes_r, name='ingredientes receta'),
    #recetas de un ingrediente
    path('ingrediente/<int:ingrediente_id>/recetas', views.index_recetas_i, name='recetas ingrediente'),
    #recetas de un tipo
    path('tipo/<int:tipo_id>/recetas', views.index_recetas_t, name='recetas tipo')

]