#Escribir un programa que sume los números de una lista y devuelva el resultado. 
# El programa debe preguntar al usuario cuántos números desea ingresar en la lista, 
# y luego pedir que se ingresen esos números. (Incluir: ciclos for, listas y arreglos, funciones)
lista_n = []
def agregarNumeros(numeros):
    for x in range((numeros)):
        n_x = int(input(f'Ingrese número {x+1}: '))
        lista_n.append(n_x)
    print("La lista es: ", lista_n)        
    print("La suma de los numeros es: ", sum(lista_n))
cantidad_numeros = int(input("Ingrese cantidad de numeros a agregar: "))
agregarNumeros(cantidad_numeros)