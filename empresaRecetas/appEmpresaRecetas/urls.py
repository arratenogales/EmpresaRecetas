from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_recetas, name='index'),
    path('receta/<int:receta_id>/', views.show_receta, name='detail'),
    path('receta/<int:receta_id>/ingredientes', views.index_ingredientes, name='ingredientes'),
    path('ingrediente/<int:ingrediente_id>', views.show_ingrediente, name='ingrediente'),
    path('tipo/<int:tipo_id>', views.show_tipo, name='tipo'),

]