from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Departamento

def listar_departamentos(request):
    all_dep = Departamento.objects.all()
    lista_dep = []
    for i in all_dep:
        dict = {}
        nombre = i.nombre
        cod_dep = i.cod_departmento
        dict['Nombre_departamento'] = nombre
        dict['Codigo_departamento'] = cod_dep
        lista_dep.append(dict)
    return JsonResponse(lista_dep, safe=False)
