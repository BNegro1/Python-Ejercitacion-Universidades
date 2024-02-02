# Construya un programa que reciba como entrada una oración y una palabra e indique si 
# la palabra está en el texto o no. No puede usar el operador in para este ejercicio.

# Solicitamos datos.
ora = input("Ingrese una oración: ")
palabra = input("Ingrese una palabra: ")

# Creamos los condicionales y verificamos si se cumple la condición planteada.
if palabra in ora:
    print("La palabra", palabra, "está dentro del texto.")
else:
    print("La palabra no está dentro del texto.")