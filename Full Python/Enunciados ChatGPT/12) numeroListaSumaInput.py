#Escribir un programa que sume los números de una lista y devuelva el resultado. 
#El programa debe preguntar al usuario cuántos números desea ingresar en la lista, 
#y luego pedir que se ingresen esos números. (Incluir: ciclos for, listas y arreglos, funciones)

def ingresoNumero(numero):
    lista_n = []
    for x in range(numero):
        input_l = int(input(f"Ingrese numero {x+1}: "))
        lista_n.append(input_l)
    print("La suma de la lista es: ",sum(lista_n))
    
n = int(input("Ingrese cantidad números: "))
ingresoNumero(n)