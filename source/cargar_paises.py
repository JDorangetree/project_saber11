import pandas as pd

df = pd.read_excel('paises/COD_PAISES.xlsx')
nombres = list(df[df.columns[0]])
cod_pais = list(df[df.columns[1]])
data = []
for i in range(0, len(nombres)):
    dict = {}
    dict['nombre'] = nombres[i]
    dict['cod_pais'] = cod_pais[i]
    data.append(dict)

from paises.models import Pais 

for datos in data:
    obj = Pais(**datos)
    obj.save()
