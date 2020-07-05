from django.db import models

class Departamento(models.Model):
    """Departamentos model"""

    nombre = models.CharField(max_length=100, unique=True)
    cod_departmento = models.PositiveIntegerField(unique=True, primary_key=True)
