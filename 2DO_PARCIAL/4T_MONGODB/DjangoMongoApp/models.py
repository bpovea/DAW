from djongo import models

# Create your models here.
class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    fecha = models.DateField()
    totalFactura  = models.FloatField()

    def __str__(self):
        return 'Servicio: {}:{}'.format(self.id, self.nombre)
   

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=75)
    ciudad = models.CharField(max_length=75)
    servicios = models.EmbeddedModelField(model_container=Servicio)

    def __str__(self):
        return 'Usuario: {}:{}'.format(self.nombre_completo, self.ciudad)

