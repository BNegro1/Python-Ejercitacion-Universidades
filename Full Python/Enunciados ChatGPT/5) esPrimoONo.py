#Escriba un programa que determine si un número dado es primo o no.
def es_primo(n):
    if n < 2:
        print("Ingrese un numero mayor a 2.")
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Ingrese numero para saber si es primo o no:"))
es_primo(n)
