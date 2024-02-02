#1. Construya un programa en Python que cuente la cantidad de vocales y consonantes en un texto.

# Definimos la variable "vo" y "co" respectivamente, para contar en cada iteración.
vo = 0
co = 0

# Definimos la listas con vocales y consonantes.
vocales = ["a","e","i","o","u"]
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", 
               "m", "n", "ñ", "p", "q", 
               "r", "s", "t", "v", "w", "x", "y", "z"]

# Pedimos datos
texto = input("Ingrese texto: ")

# Iniciamos ciclo para comprobar.
for x in texto:
    if x in vocales: # Se comprueba el iterador "x" en la lista vocales
        vo = vo + 1 # Se suma una unidad a la variable "vo" en caso de cumplir la condición.
    elif x in consonantes: # Sino, se comprueba en la lista de consonantes.
        co = co + 1 # Sino, se suma una unidad a la variable "co" en caso de cumplir la condición.
        
# Imprimimos los resultados.
print("Total de vocales: ", vo)
print("Total de consonantes: ", co)

