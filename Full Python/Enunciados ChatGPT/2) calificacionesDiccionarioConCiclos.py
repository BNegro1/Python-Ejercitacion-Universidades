#Crea un diccionario que almacene las calificaciones de un estudiante (nombre del estudiante: calificación).

estudiantes_l = []
dict_total = {}



inp_e = int(input("Cantidad de estudiantes: "))
inp_n = int(input("Cantidad de notas: "))

for x in range(inp_e):
    nombre = (input(f'Ingrese nombre del estudiante {x+1}: '))
    notas_l = []    # cada vez que se recorre el bucle, se crea una nueva lista de notas vacía para almacenar las notas del estudiante actual.
                    # Si se creara la lista fuera del bucle, todas las notas ingresadas se acumularían en la misma lista y se 
                    # asignarían a todos los estudiantes en el diccionario "dict_total", en lugar de asignarse solo al estudiante actual.
    for i in range(inp_n):
        nota_x = float(input(f"Ingrese nota {i+1} del estudiante {nombre}: "))
        notas_l.append(nota_x)
    dict_total[nombre] = notas_l # Agrega un nuevo elemento al diccionario "dict_total".
                                 # El nombre del estudiante (variable "nombre") es utilizada como la clave / key del diccionario,
                                 # y la lista de notas del estudiante (variable "notas_l") es utilizada como el valor / value correspondiente.
                                 # Relacion = Nombre : Nota
                                 # Si se repite el nombre, se le asignara el valor nuevo / actual que se le ingrese
                                 # Se puede usar OrderedDict para realizar la repetición (Investigar.)

print("El diccionario con todas las notas es: ")
print(dict_total)