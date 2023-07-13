from django import forms


class ProfesorFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    profesion=forms.CharField()

class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    dni=forms.IntegerField()
    email=forms.EmailField()

class AsignaturasFormulario(forms.Form):
    asignatura=forms.CharField(max_length=40)
    programaEstudio=forms.IntegerField()
    catedra=forms.CharField(max_length=40)
    