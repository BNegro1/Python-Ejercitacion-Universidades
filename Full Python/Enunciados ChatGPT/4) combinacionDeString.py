import random

def randomize_string(string):
    # Convertir la cadena en una lista de caracteres
    lista_caracter = list(string)
    # Utilizar la función shuffle para barajar los caracteres de forma aleatoria
    random.shuffle(lista_caracter)
    # Convertir la lista de caracteres de nuevo en una cadena
    alea = ''.join(lista_caracter)
    return alea

original_string = input("Ingrese string: ")
for x in range(len(original_string)): # Ciclo para hacer combinaciones
    randomized_string = randomize_string(original_string)
    print(randomized_string, end = ', ')
    