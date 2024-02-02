#Crea un programa que genere una lista de números armónicos hasta un número dado.
n = int(input("Ingrese un número entero positivo: "))
harmonic_list = []
total = 0

for i in range(1, n+1):
    total += 1/i
    harmonic_list.append(total)

print("Los números armónicos hasta", n, "son:", harmonic_list)
