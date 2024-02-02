#Escriba un programa que calcule la suma de los primeros 100 números naturales.

naturales = []
for x in range(0, 101):
    naturales.append(x)
print("La suma de los 100 primeros numeros naturales es: ", sum(naturales))