from rest_framework import status
from rest_framework.response import Response
from ..serializers import *
from django.http import Http404
from rest_framework.views import APIView
import datetime

class usuario_servicio(APIView):

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
        servicioUsuario =  usuario.servicios.filter(servicio=servicio)
        if servicioUsuario:
            servicioUsuario.update(direccion=request.POST['direccion'])
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        else:
            return Response("Ya esta registrado ese servicio", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        servicio = Servicio.objects.get(nombre=request.POST['servicio'])
        usuario.servicios.filter(servicio=servicio).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)