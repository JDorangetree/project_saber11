from django.urls import path

from .views import listar_colegios, listar_cole_municipio

urlpatterns = [
    path('lista/', listar_colegios),
    path('lista/<nombre>', listar_cole_municipio),
]
