#Crea un programa que calcule el mínimo común múltiplo (MCM) de dos números dados.

def gcd(a, b):
    while b:
        a, b = b, a % b # Asignación multiple (permuta los valores de a y b)
    return print(a)
n1 = int(input("Ingrese n1: "))
n2 = int(input("Ingrese n2: "))
gcd(n1, n2)
