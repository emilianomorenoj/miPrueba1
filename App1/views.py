from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
# Create your views here.


def familiar(request):

    fam = familiares(nombre="Ricardo Moreno", edad=58, fechanacimiento=6-2-1964)
    fam.save()

    return HttpResponse(f"Mi familiar se llama:  {fam.nombre} , tiene {fam.edad} años y naciò el {fam.fechanacimiento} ")

def entregables(request):

    entre1 = Entregable(nombre="Examen 1", fechaEntrega="2022-09-08")
    entre1.save()

    return HttpResponse(f"He guardado: {entre1.nombre} con fecha {entre1.fechaEntrega}")