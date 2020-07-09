from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Estudiantes

def listar_estudiantes(request):
    return HttpResponse('Hola')
