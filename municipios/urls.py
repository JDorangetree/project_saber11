from django.urls import path

from .views import listar_municipios

urlpatterns = [
    path('lista/', listar_municipios),
]
