from rest_framework import serializers
from .models import *

class ServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicio
		fields = "__all__"

class ServicioUsuarioSerializer(serializers.ModelSerializer):
	servicio = ServicioSerializer()
	class Meta:
		model = ServicioUsuario
		fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
	servicios = ServicioUsuarioSerializer(many=True)
	class Meta:
		model = Usuario
		fields = "__all__"

