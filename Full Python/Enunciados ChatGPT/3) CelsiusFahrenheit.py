#Escriba un programa que convierta una lista de grados Celsius a grados Fahrenheit.

celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = []
for x in celsius:
    f = (9/5)*x+32
    fahrenheit.append(f)
print(fahrenheit)