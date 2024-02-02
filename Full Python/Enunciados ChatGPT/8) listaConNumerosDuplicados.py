# Crea una función que tome una lista de números como entrada y 
# devuelva una nueva lista con los números duplicados eliminados.

def eliminar_duplicados(numbers):
    # Crea una lista vacía para almacenar números sin duplicados
    sin_duplicados = []
    # Recorre la lista de números de entrada
    for num in numbers:
        # Si el número actual no está en la lista sin duplicados, agrégalo
        if num not in sin_duplicados:
            sin_duplicados.append(num)
    # Devuelve la lista sin duplicados
    return sin_duplicados

# Pide al usuario la cantidad de números a ingresar
cantidad_numeros = int(input("Ingrese cantidad de numeros a ingresar: "))
# Crea una lista vacía para almacenar los números de entrada
numbers = []
# Pide al usuario que ingrese los números
for x in range(cantidad_numeros):
    numeros_input = int(input(f"Ingrese numero {x+1}: "))
    # Agrega el número de entrada a la lista
    numbers.append(numeros_input)
# Llama a la función para eliminar duplicados y almacena su resultado en una variable
sin_duplicados = eliminar_duplicados(numbers)
# Imprime la lista original y la lista sin duplicados
print("Lista original: ", numbers)
print("Lista sin duplicados: ", sin_duplicados)
