from django.shortcuts import render
from django.http import HttpResponse
from ProyectoApp.models import *
from ProyectoApp.forms import *
# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')

def estudiantes(request):

    return render(request, 'estudiante.html')

#def profesores(request):

    return render(request, 'profesor.html')

#def asignatura(request):

    return render(request, 'asignatura.html')


def asignatura(request):

    if request.method == 'POST':
        miFormulario = AsignaturasFormulario(request.POST)#aca llega la info del HTML
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            asignatur = AsignaturasFormulario(asignatura=informacion['asignatura'], 
                                          programaEstudio=informacion['programaEstudio'], 
                                          catedra=informacion['catedra'],)
            asignatur.save()
            return render(request, 'inicio.html')
    else: 
        miFormulario= AsignaturasFormulario()

    return render(request, r'asignatura.html', {'miFormulario': miFormulario})

def profesores(request):

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)#aca llega la info del HTML
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            profesor = ProfesorFormulario(nombre=informacion['nombre'], 
                                          apellido=informacion['apellido'], 
                                          email=informacion['email'],
                                          profesion=informacion['profesion'])
            profesor.save()
            return render(request, 'inicio.html')
    else: 
        miFormulario= ProfesorFormulario()

    return render(request, r'profesor.html', {'miFormulario': miFormulario})

def estudianteFormulario(request):

    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)#aca llega la info del HTML
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            estudiante = EstudianteFormulario(nombre=informacion['nombre'], 
                                          apellido=informacion['apellido'], 
                                          dni=informacion['dni'],
                                          email=informacion['email'])
            estudiante.save()
            return render(request, 'inicio.html')
    else: 
        miFormulario= EstudianteFormulario()

    return render(request, r'formularios/estudianteFormulario.html', {'miFormulario': miFormulario})