# Generated by Django 4.2.2 on 2023-07-13 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignaturas',
            name='profesion',
        ),
    ]