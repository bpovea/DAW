from django.db import models

# Create your models here.
class Usuario(models.Model):
    ci = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    fecha = models.DateTimeField(auto_now_add=True)
    servicios = models.ManyToManyField('Servicio')

    def __str__(self):
        return 'Usuario: {}:{}'.format(self.ci, self.fecha)

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=35)

    def __str__(self):
        return 'Servicio: {}:{}'.format(self.id, self.nombre)
   