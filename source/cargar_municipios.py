import pandas as pd
from municipios.models import Municipio 
from departamentos.models import Departamento

df = pd.read_excel('/home/julian/proyecto_icfes/municipios/COD_MUNICIPIOS.xlsx')
nombres = list(df[df.columns[0]])
cod_mun = list(df[df.columns[1]])
cod_dep = list(df[df.columns[2]])
data = []
for i in range(0, len(nombres)):
    dict = {}
    dict['nombre'] = nombres[i]
    dict['cod_municipio'] = cod_mun[i]
    dict['cod_departamento'] = Departamento.objects.get(cod_departmento=cod_dep[i])
    data.append(dict)

for datos in data:
    obj = Municipio(**datos)
    obj.save()
