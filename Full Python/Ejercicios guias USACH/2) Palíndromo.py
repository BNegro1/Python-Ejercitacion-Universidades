# 2. Construya un programa en Python que indique si un texto entregado es palíndromo o no, 
# considere que un palíndromo es una palabra que se lee igual de derecha a izquierda y 
# de izquierda a derecha.

# Solicitamos el texto.
texto = input("Ingrese texto: ")

if texto[::-1] == texto: # Comprobamos que el texto original sea igual al palindromo.
    print("Es palindromo.")
else:
    print("No es palindromo.")