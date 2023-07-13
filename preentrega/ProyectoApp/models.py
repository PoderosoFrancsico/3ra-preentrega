from django.db import models

# Create your models here.
class Estudiante(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)

class Asignaturas(models.Model):
    asignatura=models.CharField(max_length=40)
    programaEstudio=models.IntegerField()
    catedra=models.CharField(max_length=40)
    