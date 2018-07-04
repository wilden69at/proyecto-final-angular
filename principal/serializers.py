from rest_framework import serializers
from .models import Autor,Entrada

class AutorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Autor
		fields=('id','documento','nombre','fecha_nac')

class EntradaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Entrada
		fields=('id','titulo','contenido','autor')