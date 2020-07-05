import pandas as pd
from municipios.models import Municipio
from departamentos.models import Departamento
from colegios.models import Colegios

df = pd.read_excel('/home/julian/proyecto_icfes/colegios/COLEGIOS.xlsx')
cod_mun = list(df[df.columns[13]])
cod_dep = list(df[df.columns[14]])
print(cod_dep)
data = []
for i in range(0, len(cod_mun)):
    dict = {}
    dict['cod_colegio'] = list(df[df.columns[0]])[i]
    dict['cod_dane'] = list(df[df.columns[1]])[i]
    dict['nombre'] = list(df[df.columns[2]])[i]
    dict['genero'] = list(df[df.columns[3]])[i]
    dict['naturaleza'] = list(df[df.columns[4]])[i]
    dict['calendario'] = list(df[df.columns[5]])[i]
    dict['bilingue'] = list(df[df.columns[6]])[i]
    dict['caracter'] = list(df[df.columns[7]])[i]
    dict['cod_dane_sede'] = list(df[df.columns[8]])[i]
    dict['nombre_sede'] = list(df[df.columns[9]])[i]
    dict['sede_principal'] = list(df[df.columns[10]])[i]
    dict['area_ubicacion'] = list(df[df.columns[11]])[i]
    dict['jornada'] = list(df[df.columns[12]])[i]
    dict['cod_municipio_ubicacion'] = Municipio.objects.get(cod_municipio=cod_mun[i])
    dict['cod_departamento_ubicacion'] = Departamento.objects.get(cod_departmento=cod_dep[i])
    data.append(dict)
    print(i)

for datos in data:
    obj = Colegios(**datos)
    obj.save()
