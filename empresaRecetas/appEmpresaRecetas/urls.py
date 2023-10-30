from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('appEmpresaRecetas/', include('appEmpresaRecetas.urls')),
    path('admin/', admin.site.urls),
    #prueba
]