from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=35)
    ciudad = models.CharField(max_length=75)
    servicios = models.ManyToManyField('Servicio')
    
    def __str__(self):
        return 'Usuario: {}:{}'.format(self.nombre, self.ciudad)

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=35)
    fecha = models.DateField()
    totalFactura  = models.FloatField()
    direccion = models.CharField(max_length=100)
    def __str__(self):
        return 'Servicio: {}:{}'.format(self.id, self.nombre)
   