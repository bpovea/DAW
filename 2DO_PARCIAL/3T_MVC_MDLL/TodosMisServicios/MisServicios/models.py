from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=35)
    ciudad = models.CharField(max_length=75)
    
    def __str__(self):
        return 'Usuario: {}:{}'.format(self.nombre, self.ciudad)

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=35)
    
    def __str__(self):
        return 'Servicio: {}:{}'.format(self.id, self.nombre)

class ServicioUsuario(models.Model):
    usuario = models.ForeignKey('Usuario',related_name="servicios", on_delete=models.CASCADE)
    servicio = models.ForeignKey('Servicio',related_name="usuarios", on_delete=models.CASCADE)
    fecha = models.DateField()
    totalFactura  = models.FloatField(null=True)
    direccion = models.CharField(max_length=100)