from django.db import models

# Create your models here.

class Reserv(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    correo=models.EmailField(null=True, blank=True)
    telefono=models.CharField(max_length=20)
    numPersonas=models.CharField(max_length=3)
    fecha=models.DateField()
    hora=models.TimeField()
    tipo=models.CharField(max_length=50)
    nota=models.CharField(max_length=200)
    acceso=models.CharField(max_length=100)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre,self.codigo) 