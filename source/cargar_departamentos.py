import pandas as pd

df = pd.read_excel('departamentos/COD_DEPARTAMENTOS.xlsx')
nombres = list(df[df.columns[0]])
cod_dep = list(df[df.columns[1]])
data = []
for i in range(0, len(nombres)):
    dict = {}
    dict['nombre'] = nombres[i]
    dict['cod_departmento'] = cod_dep[i]
    data.append(dict)

from departamentos.models import Departamento 

for datos in data:
    obj = Departamento(**datos)
    obj.save()
