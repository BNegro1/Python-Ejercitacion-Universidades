#Escribir un programa que convierta un 
# número decimal a binario utilizando el algoritmo de división sucesiva por 2. 
# (Incluir: ciclos while, funciones)
def decimal_a_binario(numero_decimal):
    binario = ""
    while numero_decimal >= 2:
        binario = str(numero_decimal % 2) + binario
        numero_decimal = numero_decimal // 2
    return str(numero_decimal) + binario


n = int(input("Ingrese numero decimal: "))
print("El numero es: ", decimal_a_binario(n))