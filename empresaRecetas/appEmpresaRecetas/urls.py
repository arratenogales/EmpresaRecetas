from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_portada, name='portada'),
    path('comentario/', views.index_comentarios, name='index_comentarios'),
    path('receta/', views.IndexRecetasListView.as_view, name='index_recetas'),
    path('ingrediente/', views.IndexIngredientesListView.as_view, name='index_ingrediente'),
    path('tipo/', views.IndexTiposListView.as_view, name='index_tipo'),
    path('form/', views.loginform, name='form'),
    path('receta/<int:receta_id>/',  views.RecetaDetailView.as_view, name='receta'),
    path('ingrediente/<int:ingrediente_id>/',  views.ImgredienteDetailView.as_view, name='ingrediente'),
    path('tipo/<int:tipo_id>/',  views.TipoDetailView.as_view, name='tipo'),
    path('formulario/', views.show_formulario, name='formulario')

]

