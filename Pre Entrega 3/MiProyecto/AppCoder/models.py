from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

    
class Computadora(models.Model):
    placaMadre = models.CharField(max_length=40)
    placaVideo = models.CharField(max_length=40)
    procesador = models.CharField(max_length=40)
    ram = models.CharField(max_length=40)
    fuente = models.CharField(max_length=40)
    almacenamiento = models.CharField(max_length=40)
    
class Perifericos(models.Model):
    teclado = models.CharField(max_length=40)
    mouse = models.CharField(max_length=40)
    monitor = models.CharField(max_length=40)
    headset = models.CharField(max_length=40)
    
class Videojuegos(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    plataforma = models.CharField(max_length=40)
    dificultad = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    finalizado = models.BooleanField(default=0)
    
class Plataforma(models.Model):
    nombrePlataforma = models.CharField(max_length=40)
    user = models.CharField(max_length=40)
    mail = models.EmailField()
    
    
    
    
    

    


