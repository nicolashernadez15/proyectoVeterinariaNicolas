from django.shortcuts import render, redirect
from veterinariaAPP.models import Mascota, ConsultaMedica, estetica, vacuna, cirugia, dueño
from veterinariaAPP.forms import *
from django.db.models import Avg,Sum

# Create your views here.
def index(request):
    return render(request, 'index.html')

def viewDueño(request):
    dueños = dueño.objects.all()
    return render(request, 'dueños/viewDueño.html', {'dueños':dueños})

def viewMascota(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/viewMascota.html', {'mascotas':mascotas})
    
def viewConsultas(request):
    consultas = ConsultaMedica.objects.all()
    promedio = ConsultaMedica.objects.all().aggregate(Avg('valor'))
    suma = ConsultaMedica.objects.all().aggregate(Sum('valor'))
    data = {
        'consultas':consultas,
        'promedio': promedio,
        'suma':suma
        
    }

    return render(request, 'consultas/viewConsultas.html', data)


def viewVacunas(request):
    vacunas = vacuna.objects.all()
    promedio = vacuna.objects.all().aggregate(Avg('valor'))
    suma = vacuna.objects.all().aggregate(Sum('valor'))
    data = {

    
        'vacunas':vacunas,
        'promedio': promedio,
        'suma':suma
    }
    return render(request, 'vacunas/viewVacunas.html', data)

def viewCirugias(request):
    cirugias = cirugia.objects.all()
    promedio = cirugia.objects.all().aggregate(Avg('valor'))
    suma = cirugia.objects.all().aggregate(Sum('valor'))
    data = {

        'cirugias': cirugias,
        'promedio': promedio,
        'suma':suma
    }
    return render(request, 'cirugias/viewCirugias.html', data)

def addMascota(request):
    data={
        'titulo': 'Registrar mascota',
        'form': MascotaForm()
    }
    if (request.method) == 'POST':
        formulario = MascotaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/mascotas')
        else:
            data['form'] = formulario
    return render(request, 'mascotas/formMascota.html', data)

def addConsulta(request):
    data={
        'titulo': 'Registrar consulta',
        'form': consultaForm()
    }
    if (request.method) == 'POST':
        formulario = consultaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/consultas')
        else:
            data['form'] = formulario
    return render(request, 'consultas/formConsultas.html', data)

def viewEsteticas(request):
    esteticas = estetica.objects.all()
    promedio = estetica.objects.all().aggregate(Avg('valor'))
    suma = estetica.objects.all().aggregate(Sum('valor'))
    data = {

    
        'esteticas':esteticas,  
        'promedio': promedio,
        'suma':suma
    }
    return render(request, 'esteticas/viewEsteticas.html', data)

def addEstetica(request):
    data={
        'titulo': 'Registrar estetica',
        'form': esteticaForm()
    }
    if (request.method) == 'POST':
        formulario = esteticaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/esteticas')
        else:
            data['form'] = formulario
    return render(request, 'esteticas/formEstetica.html', data)

def addVacunas(request):
    data={
        'titulo': 'Registrar vacunas',
        'form': vacunaForm()
    }
    if (request.method) == 'POST':
        formulario = vacunaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/vacunas')
        else:
            data['form'] = formulario
    return render(request, 'vacunas/formVacunas.html', data)

def addCirugia(request):
    data={
        'titulo': 'Registrar cirugias',
        'form': cirugiaForm()
    }
    if (request.method) == 'POST':
        formulario = cirugiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/cirugias')
        else:
            data['form'] = formulario
    return render(request, 'cirugias/formCirugias.html', data)

def addDueño(request):
    data={
        'titulo': 'Registrar dueño',
        'form': dueñoForm()
    }
    if (request.method) == 'POST':
        formulario = dueñoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/dueños')
        else:
            data['form'] = formulario
    return render(request, 'dueños/formDueño.html', data)

def editDueño(request,id):
    dueno = dueño.objects.get(id=id)
    data={
        'titulo': 'editar dueño',
        'form': dueñoForm(instance=dueno)
    }
    if (request.method) == 'POST':
        formulario = dueñoForm(request.POST, instance=dueno)
        if formulario.is_valid():
            formulario.save()
            return redirect('/dueños')
        else:
            data['form'] = formulario
    return render(request, 'dueños/formDueño.html', data)

def eliminarDueño(request,id):
    eliminarDueno = dueño.objects.get(id=id)
    eliminarDueno.delete()
    return redirect( '/dueños')

def editMascota(request,id):
    mascota = Mascota.objects.get(id=id)
    data={
        'titulo': 'editar mascota',
        'form': MascotaForm(instance=mascota)
    }
    if (request.method) == 'POST':
        formulario = MascotaForm(request.POST, instance=mascota)
        if formulario.is_valid():
            formulario.save()
            return redirect('/mascotas')
        else:
            data['form'] = formulario
    return render(request, 'mascotas/formMascota.html', data)

def eliminarMascota(request,id):
    eliminarMascota = Mascota.objects.get(id=id)
    eliminarMascota.delete()
    return redirect( '/mascotas')

def editConsulta(request,id):
    consulta = ConsultaMedica.objects.get(id=id)
    data={
        'titulo': 'editar consulta',
        'form': consultaForm(instance=consulta)
    }
    if (request.method) == 'POST':
        formulario = consultaForm(request.POST, instance=consulta)
        if formulario.is_valid():
            formulario.save()
            return redirect('/consultas')
        else:
            data['form'] = formulario
    return render(request, 'consultas/formConsultas.html', data)


def eliminarConsulta(request,id):
    eliminarMascota = ConsultaMedica.objects.get(id=id)
    eliminarMascota.delete()
    return redirect( '/consultas')


def editEstetica(request,id):
    estetica1 = estetica.objects.get(id=id)
    data={
        'titulo': 'editar estetica',
        'form': esteticaForm(instance=estetica1)
    }
    if (request.method) == 'POST':
        formulario = esteticaForm(request.POST, instance=estetica1)
        if formulario.is_valid():
            formulario.save()
            return redirect('/esteticas')
        else:
            data['form'] = formulario
    return render(request, 'esteticas/formEstetica.html', data)

def eliminarEstetica(request,id):
    eliminarEstetica = estetica.objects.get(id=id)
    eliminarEstetica.delete()
    return redirect( '/esteticas')

def editVacunas(request,id):
    vacuna1 = vacuna.objects.get(id=id)
    data={
        'titulo': 'editar vacuna',
        'form': vacunaForm(instance=vacuna1)
    }
    if (request.method) == 'POST':
        formulario = vacunaForm(request.POST, instance=vacuna1)
        if formulario.is_valid():
            formulario.save()
            return redirect('/vacunas')
        else:
            data['form'] = formulario
    return render(request, 'vacunas/formVacunas.html', data)

def eliminarVacunas(request,id):
    eliminarVacunas = vacuna.objects.get(id=id)
    eliminarVacunas.delete()
    return redirect( '/vacunas')

def editCirugias(request,id):
    cirugia1 = cirugia.objects.get(id=id)
    data={
        'titulo': 'editar cirugias',
        'form': cirugiaForm(instance=cirugia1)
    }
    if (request.method) == 'POST':
        formulario = cirugiaForm(request.POST, instance=cirugia1)
        if formulario.is_valid():
            formulario.save()
            return redirect('/cirugias')
        else:
            data['form'] = formulario
    return render(request, 'cirugias/formCirugias.html', data)


def eliminarCirugias(request,id):
    eliminarCirugias = cirugia.objects.get(id=id)
    eliminarCirugias.delete()
    return redirect( '/cirugias')