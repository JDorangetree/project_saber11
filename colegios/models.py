from django.db import models

class Colegios(models.Model):
    """Modelo colegio"""

    cod_colegio = models.PositiveIntegerField(unique=True, primary_key=True)
    cod_dane = models.BigIntegerField(blank=True)
    nombre = models.CharField(max_length=200, blank=False)
    genero = models.CharField(max_length=10, null=False, blank=False)
    naturaleza = models.CharField(max_length=15, blank=True)
    calendario = models.CharField(max_length=10, null=False, blank=False)
    bilingue = models.CharField(max_length=10, null=True, blank=True)
    caracter = models.CharField(max_length=20, null=True, blank=True)
    cod_dane_sede = models.BigIntegerField(blank=True)
    nombre_sede = models.CharField(max_length=200, blank=False)
    sede_principal = models.CharField(max_length=10, blank=True)
    area_ubicacion = models.CharField(max_length=20, blank=True)
    jornada = models.CharField(max_length=20, blank=True)
    cod_municipio_ubicacion = models.ForeignKey('municipios.Municipio', on_delete=models.CASCADE, null=False, blank=False)
    cod_departamento_ubicacion = models.ForeignKey('departamentos.Departamento', on_delete=models.CASCADE, null=False, blank=False)
