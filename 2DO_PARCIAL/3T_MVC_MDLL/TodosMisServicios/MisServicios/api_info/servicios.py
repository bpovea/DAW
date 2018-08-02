from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from ..serializers import *

class servicios(APIView):
    """
    Lista todos los servicios o crea un nuevo servicio.
    """
    def get(self, request, format=None):
        servicio = Servicio.objects.all()
        serializer = ServicioSerializer(servicio, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


