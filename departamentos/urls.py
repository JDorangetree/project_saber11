from django.urls import path

from .views import listar_departamentos

urlpatterns = [
    path('lista/', listar_departamentos),
]
