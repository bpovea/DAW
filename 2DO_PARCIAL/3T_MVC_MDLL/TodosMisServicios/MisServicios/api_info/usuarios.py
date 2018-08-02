from rest_framework import status
from rest_framework.response import Response
from ..serializers import *
from django.http import Http404
from rest_framework.views import APIView
import datetime

class usuarios(APIView):
    """
    Lista todos los usuarios o crea un nuevo usuario.
    """
    def get(self, request, format=None):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class usuario_detalle(APIView):

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        servicio = Servicio.objects.get(nombre=request.POST['servicio'])
        if not usuario.servicios.filter(servicio=servicio):
            usuarioServicio = ServicioUsuario(usuario=usuario,servicio=servicio,fecha = datetime.datetime.strptime(request.POST['registro'],"%Y-%m-%d"),
                direccion=request.POST['direccion'])
            usuarioServicio.save() 
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        else:
            return Response("Ya esta registrado ese servicio", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

