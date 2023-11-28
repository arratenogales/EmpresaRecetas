from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_portada, name='portada'),

    #path('receta/', views.index_recetas, name='index_recetas'),
    #path('ingrediente/', views.index_ingredientes, name='index_ingrediente'),
    #path('tipo/', views.index_tipos, name='index_tipo'),

    path('receta/', views.IndexRecetasListView.as_view, name='index_recetas'),
    path('ingrediente/', views.IndexIngredientesListView.as_view, name='index_ingrediente'),
    path('tipo/', views.IndexTiposListView.as_view, name='index_tipo'),

    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('writters/', views.show_writters, name='writters'),

    #path('receta/<int:receta_id>/', views.show_receta, name='receta'),
    #path('ingrediente/<int:ingrediente_id>/', views.show_ingrediente, name='ingrediente'),
    #path('tipo/<int:tipo_id>/', views.show_tipo, name='tipo'),

    path('receta/<int:receta_id>/',  views.RecetaDetailView.as_view, name='receta'),
    path('ingrediente/<int:ingrediente_id>/',  views.ImgredienteDetailView.as_view, name='ingrediente'),
    path('tipo/<int:tipo_id>/',  views.TipoDetailView.as_view, name='tipo'),

    path('formulario/', views.show_formulario, name='formulario')

]

