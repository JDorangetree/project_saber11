from django.db import models

class Municipio(models.Model):
    """Modelo de municipios"""

    nombre = models.CharField(max_length=100)
    cod_municipio = models.PositiveIntegerField(unique=True, primary_key=True)
    cod_departamento = models.ForeignKey('departamentos.Departamento', on_delete=models.CASCADE, null=False, blank=False)
