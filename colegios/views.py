from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Colegios


def listar_colegios(request):
    all_col = Colegios.objects.all()
    lista_col = []
    for i in all_col:
        dict = {}
        dict['Codigo icfes'] = i.cod_colegio
        dict['Nombre colegio'] = i.nombre
        dict['Municipio'] = i.cod_municipio_ubicacion.nombre
        dict['Departamento'] = i.cod_departamento_ubicacion.nombre
        lista_col.append(dict)
    return JsonResponse(lista_col, safe=False)

def listar_cole_municipio(request, nombre):
    all_col = Colegios.objects.filter(cod_municipio_ubicacion__nombre=nombre)
    lista_col = []
    for i in all_col:
        dict = {}
        dict['Codigo icfes'] = i.cod_colegio
        dict['Nombre colegio'] = i.nombre
        dict['Municipio'] = i.cod_municipio_ubicacion.nombre
        dict['Departamento'] = i.cod_departamento_ubicacion.nombre
        lista_col.append(dict)
    return JsonResponse(lista_col, safe=False)