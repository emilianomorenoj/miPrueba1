from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def saludo(request):
    
    nombre = "Emiliano"

    nacionalidad = "Mexicano"

    horaActual = datetime.now()

    intereses = ["MTB", "TrailRunning","KK"]

    diccionario = {"name":nombre,"country":nacionalidad,"hora": horaActual,"hobbies": intereses}

    plantilla = loader.get_template("saludar.html")

    documento = plantilla.render(diccionario)

    #miHtml = open("C:/Users/emore/OneDrive/Escritorio/Proyecto_Web_Python/Proyecto1/Proyecto1/plantillas/saludar.html")

    #plantilla = Template(miHtml.read())

    #miHtml.close()

    #miContexto = Context(diccionario)

    #documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)



def sumar(request):
    return HttpResponse("En esta pag voy a sumar nùmeros")


def miNombre(self, nombre):
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)

def calcular(request):
       tiempoActual = datetime.now()

       miCumple = datetime(2022,11,29)

       tiempoFalta = miCumple-tiempoActual

       resultadoMinutos = tiempoFalta.days * 64*24 + tiempoFalta.seconds//60

       return HttpResponse(resultadoMinutos)


def probandoTemplate(self):

    miHtml = open("C:/Users/emore/OneDrive/Escritorio/Proyecto_Web_Python/Proyecto1/Proyecto1/plantillas/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

