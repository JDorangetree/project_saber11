from django.urls import path
from .views import listar_estudiantes

urlpatterns = [
    path('lista/', listar_estudiantes),
]
