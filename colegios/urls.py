from django.urls import path

from .views import listar_colegios

urlpatterns = [
    path('lista/', listar_colegios),
]
