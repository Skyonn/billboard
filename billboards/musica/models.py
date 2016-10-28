from django.db import models
from django.utils import timezone

# Create your models here.

class Lista(models.Model):
	puesto = models.IntegerField()
	#fechalista = models.DateField()
	semana = models.IntegerField()
	cancion = models.ForeignKey('Cancion')
	
	class Meta:
		ordering = ["-puesto"]
	
	def __unicode__(self):
		return self.name

class Cancion(models.Model):
	nomcancion = models.TextField()
	autor = models.TextField()
	album = models.TextField()
	duracion = models.IntegerField()
	popularidad = models.IntegerField()
	uri = models.TextField()
	spotify = models.TextField()
