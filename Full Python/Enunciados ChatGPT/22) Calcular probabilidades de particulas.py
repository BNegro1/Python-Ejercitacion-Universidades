#Implementar un algoritmo para 
#calcular las probabilidades de encontrar una partícula en 
#diferentes posiciones en una caja cuántica

import numpy as np

# Definimos la función que calcula las probabilidades
def calcular_probabilidades(psi, rango_x):
    # Primero, calculamos la probabilidad en cada posición
    probabilidades = np.abs(psi)**2
    
    # Normalizamos la suma de las probabilidades a 1
    normalizacion = np.sum(probabilidades)
    probabilidades = probabilidades / normalizacion
    
    # Devolvemos las probabilidades normalizadas
    return probabilidades

# Definimos la función de onda de la partícula en la caja cuántica
def funcion_onda(x, n, L):
    psi = np.sqrt(2/L) * np.sin(n * np.pi * x / L)
    return psi

# Definimos los parámetros de la caja cuántica
L = float(input("Ingrese tamaño de la caja: "))  # Tamaño de la caja
n = float(input("Ingrese número cuántico (comportaiento en el sistema cuántico): "))  # Número cuántico

# Creamos un rango de posiciones para evaluar la función de onda
x_range = np.linspace(0, L, 1000)

# Evaluamos la función de onda en cada posición
psi = funcion_onda(x_range, n, L)

# Calculamos las probabilidades de encontrar la partícula en cada posición
probabilidades = calcular_probabilidades(psi, x_range)
print("Probabilidades de encontrar la partícula en cada posición:")
print(probabilidades)