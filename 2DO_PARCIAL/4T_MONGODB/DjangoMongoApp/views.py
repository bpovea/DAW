from django.shortcuts import render
from .models import *
import datetime
import csv

# Create your views here.
def lista(request):
    #registrarDatos()
    cargardatosCSV()
    usuarios = Usuario.objects.all()
    return render(request,'DjangoMongoApp/lista.html',{'usuarios':usuarios})

def registrarDatos():
    servicio1 = Servicio(nombre='Energia electrica',descripcion='descripcion energia electrica')
    servicio2 = Servicio(nombre='agua',descripcion='descripcion agua')
    servicio3 = Servicio(nombre='telefonia movil',descripcion='descripcion telefonia movil')
    servicio4 = Servicio(nombre='telefonia fija',descripcion='descripcion telefonia fija')
    
    servicio1.save()
    servicio2.save()
    servicio3.save()
    servicio4.save()

    usuario1 = Usuario(ci ='0923261382',nombre = 'Mauricio', apellidos = 'Leiton',fecha = datetime.datetime.strptime("2017-01-12","%Y-%m-%d"))
    usuario1.save()
    usuario1.servicios.add(servicio1, servicio2)

    usuario2 = Usuario(ci ='0923261383',nombre = 'David', apellidos = 'Lazaro',fecha = datetime.datetime.strptime("2018-01-12","%Y-%m-%d"))
    usuario2.save()
    usuario2.servicios.add(servicio1, servicio2,servicio3)

    usuario3 = Usuario(ci ='0923261384',nombre = 'Byron', apellidos = 'Povea',fecha = datetime.datetime.strptime("2019-01-12","%Y-%m-%d"))
    usuario3.save()
    usuario3.servicios.add(servicio4,servicio3)

def cargardatosCSV():
    import os
    print(os.getcwd())
    with open('DjangoMongoApp/data/example.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
