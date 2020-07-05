from django.urls import path

from .views import listar_paises

urlpatterns = [
    path('lista/', listar_paises),
]
