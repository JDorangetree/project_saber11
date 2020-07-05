from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pais

def listar_paises(request):
    all_pais = Pais.objects.all()
    lista_pais = []
    for i in all_pais:
        dict = {}
        nombre = i.nombre
        cod_pais = i.cod_pais
        dict['Nombre_pais'] = nombre
        dict['Codigo_pais'] = cod_pais
        lista_pais.append(dict)
    return JsonResponse(lista_pais, safe=False)
