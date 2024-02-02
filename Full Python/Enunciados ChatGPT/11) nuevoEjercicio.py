#Escribir un programa que calcule la suma de los primeros N números naturales, 
# donde N es un número dado por el usuario. (Incluir: ciclos for, funciones, condicionales)
def suma_n_numeros_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

while True: 
    natural = int(input("Ingrese cantidad de números naturales: "))    
    if natural > 0:
        resultado = suma_n_numeros_naturales(natural)
        print("La suma de los primeros", natural, "números naturales es:", resultado)
        break
    else:
        print("Ingrese un número natural.")
