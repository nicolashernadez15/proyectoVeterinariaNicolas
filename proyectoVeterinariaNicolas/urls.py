"""proyectoVeterinariaNicolas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from veterinariaAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('dueños/',views.viewDueño, name='dueños'),
    path('addDueño/',views.addDueño, name='addDueño'),
    path('mascotas/',views.viewMascota, name='mascotas'),
    path('consultas/',views.viewConsultas, name='consultas'),
    path('addMascota/',views.addMascota, name='addMascota'),
    path('addConsulta/',views.addConsulta, name='addConsulta'),
    path('esteticas/',views.viewEsteticas, name='esteticas'),
    path('addEstetica/',views.addEstetica, name='addEstetica'),
    path('vacunas/',views.viewVacunas, name='vacunas'),
    path('addVacunas/',views.addVacunas, name='addvacunas'),
    path('cirugias/',views.viewCirugias, name='cirugias'),
    path('addCirugia/',views.addCirugia, name='addcirugia'),
    path('editDueño/<int:id>', views.editDueño, name='editDueño'),
    path('eliminarDueño/<int:id>', views.eliminarDueño, name='eliminarDueño'),
    path('editMascota/<int:id>', views.editMascota, name='editMascota'),
    path('eliminarMascota/<int:id>', views.eliminarMascota, name='eliminarMascota'),
    path('editConsulta/<int:id>', views.editConsulta, name='editConsulta'),
    path('eliminarConsulta/<int:id>', views.eliminarConsulta, name='eliminarConsulta'), 
    path('editEstetica/<int:id>', views.editEstetica, name='editEstetica'),
    path('eliminarEstetica/<int:id>', views.eliminarEstetica, name='eliminarEstetica'), 
    path('editVacunas/<int:id>', views.editVacunas, name='editVacunas'),
    path('eliminarVacunas/<int:id>', views.eliminarVacunas, name='eliminarVacunas'),
    path('editCirugias/<int:id>', views.editCirugias, name='editCirugias'),
    path('eliminarCirugias/<int:id>', views.eliminarCirugias, name='eliminarCirugias'),

]
