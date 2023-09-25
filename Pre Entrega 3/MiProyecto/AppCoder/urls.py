from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("compus/", computadora, name = "Compus"),
    path("perif/", perifericos, name = "Perif"),
    path("juegos/", videojuego, name = "Juegos"),
    path("platfo/", plataforma, name = "Platfo"),
    
    #urls de creacion
    path("formuCompu/", compuFormulario, name = "CompuFormulario"),
    path("formuPerif/", periFormulario, name = "PeriFormulario"),
    path("formuJuegos/", juegoFormulario, name = "JuegoFormulario"),
    path("formuPlata/", plataFormulario, name = "PlataFormulario"),
    
    #urls de busqueda
    path("busquedaPlacaVideo/", busquedaPlacaVideo, name = "BusquedaPlacaVideo"),
    path("busquedaTeclado/", busquedaTeclado, name = "BusquedaTeclado"),
    path("busquedaVideojuego/", busquedaJuego, name = "BusquedaJuego"),
    path("busquedaPlata/", busquedaPlata, name = "BusquedaPlata"),
    
    #urls de resultado
    path("resultadoPlacaVideo/", resultadoPlacaVideo, name = "ResultadoPlacaVideo"),
    path("resultadoTeclado/", resultadoTeclado, name = "ResultadoTeclado"),
    path("resultadoJuego/", resultadoJuego, name = "ResultadoJuego"),
    path("resultadoPlata/", resultadoPlata, name = "ResultadoPlata"),
]
