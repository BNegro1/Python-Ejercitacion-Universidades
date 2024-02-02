#Escriba un programa que imprima los números pares entre 1 y 100.
#Escriba un programa que imprima los números impares entre 1 y 100.
pares = []
impares = []
for x in range(100):
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
t1 = len(pares)
t2 = len(impares)
print(f"La cantidad de numeros pares entre 1 y 100 son: {t1}")
print(pares)
print()
print(f"La cantidad de numeros impares entre 1 y 100 son: {t2}")
print(impares)