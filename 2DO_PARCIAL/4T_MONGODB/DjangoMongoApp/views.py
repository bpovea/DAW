from django.shortcuts import render
from .models import *
import csv
from datetime import datetime
# Create your views here.
def lista(request):
    #cargardatosCSV()
    usuarios = Usuario.objects.all()[0:10]
    return render(request,'DjangoMongoApp/lista.html',{'usuarios':usuarios})


def cargardatosCSV():
    Usuario.objects.all().delete()
    with open('DjangoMongoApp/data/todosmisservicios.csv') as File:
        reader = csv.reader(File, delimiter=';', quotechar=';',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            Usuario(nombre_completo=row[0], servicios=Servicio(nombre=row[1], fecha=datetime.strptime(row[3],"%Y-%m-%d"),totalFactura=row[4]),ciudad=row[2] ).save()

def filtro(request):
    servicio = request.GET.get('servicio')
    fecha = request.GET.get('fecha')
    print(fecha)
    usuarios = Usuario.objects.filter(servicios={'nombre': servicio})
    usuarios = usuarios.filter(servicios={'fecha':datetime.strptime(fecha,"%Y-%m-%d")})
    return render(request,'DjangoMongoApp/lista.html',{'usuarios':usuarios})