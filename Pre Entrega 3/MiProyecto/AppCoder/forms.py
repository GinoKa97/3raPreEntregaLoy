from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class CompuFormulario(forms.Form):
    placa_madre = forms.CharField(max_length=40)
    placa_de_video = forms.CharField(max_length=40)
    procesador = forms.CharField(max_length=40)
    ram = forms.CharField(max_length=40)
    fuente = forms.CharField(max_length=40)
    almacenamiento = forms.CharField(max_length=40)
    
class PeriFormulario(forms.Form):
    teclado = forms.CharField(max_length=40)
    mouse = forms.CharField(max_length=40)
    monitor = forms.CharField(max_length=40)
    headset = forms.CharField(max_length=40)
    
class JuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    plataforma = forms.CharField(max_length=40)
    dificultad = forms.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    finalizado = forms.BooleanField()
    
class PlataFormulario(forms.Form):
    nombre_plataforma = forms.CharField(max_length=40)
    user = forms.CharField(max_length=40)
    mail = forms.EmailField()