from django.urls import path, include
from ProyectoApp import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Estudiante', views.estudiantes, name='estudiante'),
    path('Profesor', views.profesores, name='profesor'),
    path('Asignatura', views.asignatura, name='asignatura'),
    path('estudianteFormulario', views.estudianteFormulario, name='estudianteFormulario'),
]
