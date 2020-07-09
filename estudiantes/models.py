from django.db import models

class Estudiantes(models.Model):
    """Modelo estudiantes"""

    id = models.BigIntegerField(unique=True, primary_key=True)
    estu_tipodocumento = models.CharField(max_length=10)
    cod_paisnacionalidad = models.ForeignKey('paises.Pais', on_delete=models.CASCADE, null=False, blank=False)
    genero = models.CharField(max_length=5, null=False, blank=False)
    edad = models.SmallIntegerField(null=False, blank=False)
    periodo = models.SmallIntegerField(null=False, blank=False)
    id = models.BigIntegerField(unique=True, primary_key=True)
    tiene_etnia = models.CharField(max_length=5, null=True, blank=True)
    etnia = models.CharField(max_length=100, null=True, blank=True)
    cod_municipio_reside = models.ForeignKey('municipios.Municipio', on_delete=models.CASCADE, null=False, blank=False)
    priv_libertad = models.CharField(max_length=5, null=True, blank=True)
    inse = models.FloatField(null=True, blank=True)
    nse = models.SmallIntegerField(null=True, blank=True)
    cod_colegio_estudia = models.ForeignKey('colegios.Colegios', on_delete=models.CASCADE, null=False, blank=False)