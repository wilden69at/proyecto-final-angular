from django.db import models

class Autor(models.Model):
	documento=models.BigIntegerField()
	nombre=models.CharField(max_length=200)
	fecha_nac=models.DateField()

class Entrada(models.Model):
	autor=models.ForeignKey(Autor,on_delete=models.CASCADE)	
	titulo=models.CharField(max_length=200)
	contenido=models.TextField()
	fecha=models.DateTimeField(auto_now_add=True)
