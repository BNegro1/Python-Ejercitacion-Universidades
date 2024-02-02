#Crea un programa que calcule el máximo común divisor (MCD) de dos números dados.


def mcd(numero1, numero2):
    if numero2 == 0: # Si el segundo número es igual a cero
        return numero1 # Retorna el primer número
    else: # En otro caso
        return mcd(numero2, numero1 % numero2) # Retorna el resultado de llamar la función mcd con los argumentos intercambiados y numero1 modulo numero2
n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))
print("Maximo comun divisor: ", mcd(n1, n2))