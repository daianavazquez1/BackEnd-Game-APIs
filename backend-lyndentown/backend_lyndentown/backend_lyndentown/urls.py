"""backend_lyndentown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from backend_admin.views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Personaje/<int:nombre>/', PersonajeAPI.as_view()),
    path('SeccionAPI/<int:seccionid>/', SeccionAPI.as_view()),
    path('MinigameAPI/', MinigameAPI.as_view()),
    path('HighscoreAPI/', HighscoresAPI.as_view()),
    path('inventario/', TablaInventarioAPI.as_view()),
    path('ActualizarStats/', Stats_PersonajeAPI.as_view()),
    path('Atuendos/<str:nombre>/', AtuendosAPI.as_view()),
    path('Personajespawn/', PersonajeSpawnAPI.as_view()),
    path('objectsinstance/', ObjectsInstanceAPI.as_view()),
    path('Inventory/<str:id_pj>', InventarioAPI.as_view()),
    path('personaje_posicion', Posicion_pjAPI.as_view()),
    path('getObject_instances/<str:ids>', GetObjectInstances.as_view()),
    path("RegistrartrasaccionesAPI/", PosttrasaccionesAPI.as_view()),
    path("RevisartransaccionesAPI/<str:personaje>/<int:tipo>/", GettransaccionesAPI.as_view())
]
