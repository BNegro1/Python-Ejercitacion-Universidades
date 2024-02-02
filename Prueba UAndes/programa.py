import numpy as np
import matplotlib.pyplot as plt
import csv # Importar csv EFICIENTEMENTE
def cargDatos(nombre_archivo):
    metascoreAño = {}
    userScoreAño = {}
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            meta = row['meta_score']
            user = row['user_score']
            fecha = row['date']
        
            if not meta or not user or not fecha or fecha == 'TBA':
                continue
            
            meta = float(meta)
            user = float(user) * 10 
            partes_fecha = fecha.split()
            if len(partes_fecha) == 3:
                año = int(partes_fecha[-1])
            else:
                continue
            
            if año not in metascoreAño:
                metascoreAño[año] = []
                userScoreAño[año] = []
            
            metascoreAño[año].append(meta)
            userScoreAño[año].append(user)
    
    return metascoreAño, userScoreAño

metascore, userscore = cargDatos("NintendoGames (1).csv")
def lineas(metascore, userscore):
    años = list(metascore.keys())
    promMeta = [np.mean(metascore[a]) for a in años]
    promUserSCr = [np.mean(userscore[a]) for a in años]
    
    plt.figure(figsize=(10, 6))
    plt.plot(años, promMeta, label='Meta Score Promedio')
    plt.plot(años, promUserSCr, label='User Score Promedio')
    plt.xlabel('Año')
    plt.ylabel('Puntaje Promedio')
    plt.title('Puntaje Promedio por Año')
    plt.legend()
    plt.grid(True)
    plt.show()

lineas(metascore, userscore)

def scatterr(nombre_archivo):
    genero = input("Ingrese el género de juego a comparar: ").strip().lower()
    metascore = []
    userscore = []

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            if genero in row['genres'].lower():
                meta = row['meta_score']
                user = row['user_score']
                if not meta or not user:
                    continue
                
                metascore.append(float(meta))
                userscore.append(float(user) * 10)

    if not metascore or not userscore:
        print("No se encontraron juegos para el género especificado.")
        return

    plt.figure(figsize=(8, 6))
    plt.scatter(metascore, userscore, alpha=0.5)
    plt.xlabel('Meta Score')
    plt.ylabel('User Score (x10)')
    plt.title(f'Comparación de Puntajes para el Género "{genero.capitalize()}"')
    plt.grid(True)
    plt.show()

scatterr("NintendoGames (1).csv")

def barrass(nombre_archivo):
    metaPlataf = {}
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            plataforma = row['platform']
            meta = row['meta_score']
            if not meta:
                continue
            
            meta = float(meta)
            
            if plataforma not in metaPlataf:
                metaPlataf[plataforma] = []
            
            metaPlataf[plataforma].append(meta)
    
    plataformas = list(metaPlataf.keys())
    metaScrPro = [np.mean(metaPlataf[p]) for p in plataformas]
    
    plt.figure(figsize=(12, 6))
    plt.bar(plataformas, metaScrPro)
    plt.xlabel('Plataforma')
    plt.ylabel('Meta Score Promedio')
    plt.title('Meta Score Promedio por Plataforma')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

barrass("NintendoGames (1).csv")

def guardar(nombre_archivo, palabra_clave):
    juegosEnc = []

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            if palabra_clave.lower() in row['title'].lower():
                juegosEnc.append(row)
    
    if juegosEnc:
        with open('salida.csv', 'w', newline='', encoding='utf-8') as salida:
            campos = juegosEnc[0].keys()
            writer = csv.DictWriter(salida, fieldnames=campos)
            writer.writeheader()
            writer.writerows(juegosEnc)
        print(f'Se encontraron {len(juegosEnc)} juegos y se guardaron en salida.csv.')
    else:
        print("No se encontraron juegos con la palabra clave especificada.")

palabra_clave = input("Ingrese la palabra clave para buscar juegos: ").strip()
guardar("NintendoGames (1).csv", palabra_clave)
