from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Municipio

def listar_municipios(request):
    all_mun = Municipio.objects.all()
    lista_mun = []
    for i in all_mun:
        dict = {}
        nombre = i.nombre
        cod_mun = i.cod_municipio
        cod_dep = i.cod_departamento
        dict['Nombre_municipio'] = nombre
        dict['Codigo_municipio'] = cod_mun
        dict['Departamento'] = cod_dep.nombre
        lista_mun.append(dict)
    return JsonResponse(lista_mun, safe=False)
