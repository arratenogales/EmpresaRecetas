"""
URL configuration for empresaRecetas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from appEmpresaRecetas import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appEmpresaRecetas.urls'))
]


urlpatterns += i18n_patterns (

    path('', views.index_portada, name='portada'),

    path('receta/', views.index_recetas, name='index_recetas'),
    path('ingrediente/', views.index_ingredientes, name='index_ingrediente'),
    path('tipo/', views.index_tipos, name='index_tipo'),

    path('receta/<int:receta_id>/', views.show_receta, name='receta'),
    path('ingrediente/<int:ingrediente_id>/', views.show_ingrediente, name='ingrediente'),
    path('tipo/<int:tipo_id>/', views.show_tipo, name='tipo'),
  
    
)