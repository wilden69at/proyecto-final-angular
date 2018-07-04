from django.shortcuts import render
from rest_framework import serializers,viewsets
from .models import Autor,Entrada
from .serializers import AutorSerializer,EntradaSerializer
# Create your views here.
class  AutorAPI(viewsets.ModelViewSet):
	queryset=Autor.objects.all()
	serializer_class=AutorSerializer

class  EntradaAPI(viewsets.ModelViewSet):
	queryset=Entrada.objects.all()
	serializer_class=EntradaSerializer
		