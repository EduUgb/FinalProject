from django.db import models


# Create your models here.

class Reserv(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    correo=models.EmailField(null=True, blank=True)
    telefono=models.CharField(max_length=20)
    numPersonas=models.CharField(max_length=3)
    mesa=models.CharField(max_length=3, null=True)
    fecha=models.DateField()
    hora=models.CharField(max_length=10, null=True)
    tipo=models.CharField(max_length=50)
    nota=models.CharField(max_length=200)
    acceso=models.CharField(max_length=100)


