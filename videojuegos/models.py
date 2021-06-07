from django.db import models

# Create your models here.
class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    imagen = models.CharField(max_length=500)