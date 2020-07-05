from django.db import models

class Pais(models.Model):
    """Modelo de paises"""

    nombre = models.CharField(max_length=100)
    cod_pais = models.PositiveIntegerField(unique=True, primary_key=True)
