from django.shortcuts import render
from .models import *
import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import render,redirect,render_to_response,get_object_or_404

# Create your views here.
def lista(request):
    #registrarDatos()
    usuarios = Usuario.objects.all()
    return render(request,'MisServicios/lista.html',{'usuarios':usuarios})

def servicios_prestados(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    return render(request,'MisServicios/serviciosPrestados.html',{"id":id,"usuario":usuario})

@api_view(['GET', 'POST'])
def usuario_lista(request):
    print("dds")
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("aqui")
        print(request.data)
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detalles(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def registrarDatos():
    servicio1 = Servicio(nombre='Energia electrica',descripcion='descripcion energia electrica',fecha = datetime.datetime.strptime("2017-01-12","%Y-%m-%d"),direccion="guayaquil zona2",totalFactura =32.2)
    servicio2 = Servicio(nombre='agua',descripcion='descripcion agua',fecha = datetime.datetime.strptime("2017-01-12","%Y-%m-%d"),totalFactura =32.2)
    servicio3 = Servicio(nombre='telefonia movil',descripcion='descripcion telefonia movil',fecha = datetime.datetime.strptime("2018-01-12","%Y-%m-%d"),direccion="guayaquil zona3",totalFactura =32.2)
    servicio4 = Servicio(nombre='telefonia fija',descripcion='descripcion telefonia fija',fecha = datetime.datetime.strptime("2019-01-12","%Y-%m-%d"),direccion="guayaquil zona3",totalFactura=32.2)
    
    servicio1.save()
    servicio2.save()
    servicio3.save()
    servicio4.save()

    usuario1 = Usuario(nombre = 'Mauricio', ciudad = 'Playas')
    usuario1.save()
    usuario1.servicios.add(servicio1, servicio2,servicio3)

    usuario2 = Usuario(nombre = 'David', ciudad = 'Playas')
    usuario2.save()
    usuario2.servicios.add(servicio1, servicio2,servicio3)

    usuario3 = Usuario(nombre = 'Byron', ciudad = 'Playas')
    usuario3.save()
    usuario3.servicios.add(servicio4,servicio3,servicio1)