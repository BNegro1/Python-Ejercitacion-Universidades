# Listas sin CONSTRUCTOR

lista_corchetes = [1,2,3,4]

# La listas con CONSTRUCTOR (función list()) 
# Esta solo soporta 1 argumento

#lista = list(1,2,3,4) # Definimos la lista con 4 argumentos.
#print(lista) # Error de impresión.

# Entonces, para soportar mas argumentos en uno solo se realiza una tupla.

lista = list((1,2,3,4)) # Tupla debido al parentesis doble.
print("La lista es: ",(lista)) # Impresión de la tupla.

# Creación de lista con constructor y rango:

lista_rango = list(range(1, 100)) # range(x, y-1)
print((lista_rango))

# Información de una lista (metodos, datos, etc):

print(dir(lista))
print(dir(lista_rango))
print(dir(lista_corchetes))
