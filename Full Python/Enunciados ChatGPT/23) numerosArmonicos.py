#Crea un programa que genere una lista de números armónicos hasta un número dado.
l = [] # Crea la lista
def media_armónica(números):
    suma_inversa = 0
    for num in números: # Iterar cada numero de la lista
        suma_inversa += 1/num # Se agrega el valor a "suma_inversa"
    return print(len(números) / suma_inversa) # Devuelve el res. de la division de la longitud de la lista "numeros"

n = int(input("Ingrese largo de la lista: "))

for x in (range(1, n+1)):
    l.append(x)
print("Lista: ",l)
media_armónica(l)