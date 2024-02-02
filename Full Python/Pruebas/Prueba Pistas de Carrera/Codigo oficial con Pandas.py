



'''
Generar, para cada país participante, el archivo resultados-XX.csv, el cual debe 
registrar: apodo del competidor, correo de contacto y tiempo total empleado para completar 
las 5 vueltas. Dicho archivo NO debe incluir a los participantes que abandonan antes de 
completar la carrera. Adicionalmente, este archivo debe estar ordenado de manera creciente 
según el tiempo total.
  Generar el archivo ganadores.csv, el cual debe registrar a los 10 mejores competidores 
(que completan la carrera) a nivel global, indicando apodo del competidor, país, correo de 
contacto y tiempo total empleado para completar las 5 vueltas.
  Mostrar por pantalla el mejor tiempo para completar una única vuelta al circuito y el apodo
del(los) jugador(es) que logra(n) dicha marca, sin importar si el jugador completó la carrera.
  El archivo de tiempo siempre tendrá registros válidos, es decir, no contiene vueltas repetidas 
para un competidor ni registros faltantes (es decir, para cada participante se registran 
vueltas consecutivas)

Módulos no vistos en clases. Se permiten, sin embargo, los módulos numpy, pandas y 
matplotlib.
Construcciones que usen las palabras reservadas try y except.
Expresiones regulares.
Los tipos de dato conjunto (set), tupla (tuple) y diccionario (dict).
Programación orientada a objetos, es decir, definición de clases y métodos.
El uso de las funcio

'''


import pandas as pd

# Cargar datos en un DataFrame
df = pd.read_csv("tiempos.csv", sep=";")

# Agrupar tiempos por identificador y sumar vueltas y tiempo
df_tiempos = df.groupby(['identificador']).agg({'vuelta': 'max', 'tiempo': 'sum'}).reset_index()
#groupby agrupa los datos según el identificador y luego se usa agg para agregar las columnas vuelta y tiempo, max y sum respectivamente.
#reset_index() resetea el indice

# Cargar datos en un DataFrame
df_participante = pd.read_csv("participantes.csv", sep=";")

# Unir los dos dataframes
df_merged = pd.merge(df_tiempos, df_participante, left_on='identificador', right_on='identificador')
#merge une los dos dataframes según el identificador

# Filtrar participantes que completaron la carrera
completaron = df_merged[df_merged["vuelta"] == 5]
#selecciona solo los que completaron la carrera

# Ordenar por tiempo total
completaron = completaron.sort_values("tiempo")
#ordena por tiempo

# Guardar en archivos resultados-XX.csv
for pais in completaron["pais"].unique():
    resultados_pais = completaron[completaron["pais"] == pais]
    resultados_pais.to_csv(f"resultados-{pais}.csv", columns=["apodo", "correo", "tiempo"])
#guarda en un archivo resultados-XX.csv

# Seleccionar los 10 mejores competidores a nivel global
ganadores = completaron.head(10)
#selecciona los 10 mejores

# Guardar en archivo ganadores.csv
ganadores.to_csv("ganadores.csv", columns=["apodo", "pais", "correo", "tiempo"])
#guarda en un archivo ganadores.csv

# Obtener mejor tiempo de vuelta
mejor_vuelta = df.sort_values("tiempo").head(1)

# Obtener apodo del competidor que logró el mejor tiempo
competidor_mejor_vuelta = df_participante[df_participante["identificador"] == mejor_vuelta["identificador"].values[0]]["apodo"].values[0]

print(f"Mejor tiempo de vuelta: {mejor_vuelta['tiempo'].values[0]}")
print(f"Apodo del competidor: {competidor_mejor_vuelta}")
