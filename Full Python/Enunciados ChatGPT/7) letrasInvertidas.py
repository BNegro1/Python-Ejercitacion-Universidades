#Crea una función que tome una cadena como entrada y devuelva una nueva cadena con las letras invertidas.

def invertida(cadenita):
    for x in (cadenita):
        cadena = cadenita[::-1]
    print("Cadena nueva:", cadena)
cadena = input("Ingrese palabra para invertirla: ")
invertida(cadena)