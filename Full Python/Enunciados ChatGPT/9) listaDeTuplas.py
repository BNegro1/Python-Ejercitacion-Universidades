#Crea una lista de tuplas donde cada tupla contenga un nombre y una edad. Imprime la lista ordenada por edad.

lista_de_tuplas = []
personas = int(input("Ingrese cantidad de personas: "))
for x in range(personas):
    nombre = input(f"Ingrese nombre {x+1}: ")
    edad = int(input(f"Ingrese edad {x+1}: "))
    tupla = (nombre, edad)
    lista_de_tuplas.append(tupla) # Agrega la tupla anterior a lista de tuplas
ordenada = sorted(lista_de_tuplas, key=lambda x: x[1])  # lambda x: x[1]
                                                        # Se define mediante "key" y la variable de lambda es "x"
                                                        # Con el metodo sorte() ordena la "lista_de_tuplas" y
                                                        # con lambda la ordena, se conoce como funcion anonima: 
                                                        # "Lambda"
print(ordenada)
