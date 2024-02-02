#Crea una lista de números enteros y devuelve el valor máximo y mínimo de la lista.
from random import *
lista_l = []
for x in range(randint(1, 100)):
    lista_l.append(x)
print("Valor maximo de la lista: ", max(lista_l))
print("Valor minimo de la lista: ", min(lista_l))
print("Lista: ", lista_l)
