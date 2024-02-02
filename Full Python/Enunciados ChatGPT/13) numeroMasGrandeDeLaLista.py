#Escribir un programa que encuentre el número más grande de una lista de números. 
# (Incluir: ciclos for, listas y arreglos, funciones)

lista_n = []
def agregarNumero():
    cant_n = int(input("Ingrese cantidad de numeros a agregar: "))
    for x in range((cant_n)):
        numero_x = int(input(f"Ingrese numero {x+1}: "))
        lista_n.append(numero_x)
    print("Número mas grande de la lista: ", max(lista_n))
    print("Lista de números: ", lista_n)
    print("Suma total: ", sum(lista_n))

agregarNumero()
