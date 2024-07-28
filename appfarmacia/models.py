from django.db import models

# Create your models here.

class Medicamento(models.Model):
    nombre= models.CharField(max_length=20)
    droga= models.CharField(max_length=20)
    inventario= models.IntegerField()
    receta= models.BooleanField()
    vencimiento= models.DateField()


class Medico(models.Model):
    nombre= models.CharField(max_length=10)
    apellido= models.CharField(max_length=10)
    especialidad= models.CharField (max_length=20)
    matricula= models.IntegerField ()
    email= models.EmailField ()


class Paciente(models.Model):
    nombre= models.CharField(max_length=10)
    apellido= models.CharField(max_length=10)
    obra_social= models.CharField(max_length=20)
    nafiliado= models.IntegerField()
    email= models.EmailField()


class Proveedor(models.Model):
    nombre= models.CharField(max_length=20)
    nproveedor= models.IntegerField()
