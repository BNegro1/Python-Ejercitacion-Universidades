import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Procesar el archivo CSV
def cargar_datos(nombre_archivo):
    metascore_promedio_por_año = {}
    userscore_promedio_por_año = {}
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        next(archivo)  # Saltar la primera línea (encabezado)
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) != 9:
                continue
            
            meta_score = partes[0].strip()
            user_score = partes[4].strip()
            date = partes[3].strip()
            
            # Verificar si las puntuaciones y la fecha son válidas
            if not meta_score or not user_score or not date or date == 'TBA':
                continue
            
            try:
                meta_score = float(meta_score)
                user_score = float(user_score) * 10  # Escalar user_score al rango 0-100
            except ValueError:
                continue  # Saltar filas con valores no numéricos
            
            # Extraer el año de la fecha
            año = date.split(",")[-1].strip()
            if not año.isdigit():
                continue  # Saltar filas con fechas no válidas
            
            año = int(año)
            
            if año not in metascore_promedio_por_año:
                metascore_promedio_por_año[año] = []
                userscore_promedio_por_año[año] = []
            
            metascore_promedio_por_año[año].append(meta_score)
            userscore_promedio_por_año[año].append(user_score)
    
    return metascore_promedio_por_año, userscore_promedio_por_año

metascore_promedio, userscore_promedio = cargar_datos("NintendoGames (1).csv")

# Paso 2: Gráfico de líneas para metascore y userscore promedio por año
def grafico_lineas(metascore_promedio, userscore_promedio):
    años = list(metascore_promedio.keys())
    años.sort()  # Ordenar los años
    metascore_promedio = [np.mean(metascore_promedio[año]) for año in años]
    userscore_promedio = [np.mean(userscore_promedio[año]) for año in años]
    
    plt.figure(figsize=(10, 6))
    plt.plot(años, metascore_promedio, label='Meta Score Promedio')
    plt.plot(años, userscore_promedio, label='User Score Promedio')
    plt.xlabel('Año')
    plt.ylabel('Puntaje Promedio')
    plt.title('Puntaje Promedio por Año')
    plt.legend()
    plt.grid(True)
    plt.show()

grafico_lineas(metascore_promedio, userscore_promedio)

# Paso 3: Gráfico scatter para comparar metascore y userscore por género
def grafico_scatter_por_genero(nombre_archivo):
    genero_buscar = input("Ingrese el género de juego a comparar: ").strip().lower()
    metascore = []
    userscore = []

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        next(archivo)  # Saltar la primera línea (encabezado)
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) != 9:
                continue
            
            if genero_buscar in partes[8].lower():
                meta_score = partes[0].strip()
                user_score = partes[4].strip()
                if not meta_score or not user_score:
                    # Saltar las filas que no tienen puntuaciones válidas
                    continue
                
                try:
                    metascore.append(float(meta_score))
                    userscore.append(float(user_score) * 10)
                except ValueError:
                    continue  # Saltar filas con valores no numéricos

    if not metascore or not userscore:
        print("No se encontraron juegos para el género especificado.")
        return

    plt.figure(figsize=(8, 6))
    plt.scatter(metascore, userscore, alpha=0.5)
    plt.xlabel('Meta Score')
    plt.ylabel('User Score (x10)')
    plt.title(f'Comparación de Puntajes para el Género "{genero_buscar.capitalize()}"')
    plt.grid(True)
    plt.show()

grafico_scatter_por_genero("NintendoGames (1).csv")

# Paso 4: Gráfico de barras para metascore promedio por plataforma
def grafico_barras_por_plataforma(nombre_archivo):
    metascore_promedio_por_plataforma = {}
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        next(archivo)  # Saltar la primera línea (encabezado)
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) != 9:
                continue
            
            plataforma = partes[2].strip()
            meta_score = partes[0].strip()
            if not meta_score:
                continue
            
            try:
                meta_score = float(meta_score)
            except ValueError:
                continue  # Saltar filas con valores no numéricos
            
            if plataforma not in metascore_promedio_por_plataforma:
                metascore_promedio_por_plataforma[plataforma] = []
            
            metascore_promedio_por_plataforma[plataforma].append(meta_score)
    
    plataformas = list(metascore_promedio_por_plataforma.keys())
    metascores_promedio = [np.mean(metascore_promedio_por_plataforma[p]) for p in plataformas]
    
    plt.figure(figsize=(12, 6))
    plt.bar(plataformas, metascores_promedio)
    plt.xlabel('Plataforma')
    plt.ylabel('Meta Score Promedio')
    plt.title('Meta Score Promedio por Plataforma')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

grafico_barras_por_plataforma("NintendoGames (1).csv")

# Paso 5: Crear archivo CSV con juegos que contienen la palabra clave en el título
def buscar_y_guardar_juegos(nombre_archivo, palabra_clave):
    juegos_encontrados = []

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        next(archivo)  # Saltar la primera línea (encabezado)
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) != 9:
                continue
            
            if palabra_clave.lower() in partes[1].lower():
                juegos_encontrados.append(linea.strip())
    
    if juegos_encontrados:
        with open('salida.csv', 'w', newline='', encoding='utf-8') as salida:
            salida.write("meta_score,title,platform,date,user_score,link,esrb_rating,developers,genres\n")
            salida.write("\n".join(juegos_encontrados))
        print(f'Se encontraron {len(juegos_encontrados)} juegos y se guardaron en salida.csv.')
    else:
        print("No se encontraron juegos con la palabra clave especificada.")

palabra_clave = input("Ingrese la palabra clave para buscar juegos: ").strip()
buscar_y_guardar_juegos("NintendoGames (1).csv", palabra_clave)
