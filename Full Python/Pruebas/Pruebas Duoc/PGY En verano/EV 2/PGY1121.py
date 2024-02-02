# Evaluación 2: Python.

# Ejercicio 1

v_mas = 500

cant_mas = int(input("Ingrese cantidad de mascarillas: "))
destino_env = input("El envio es en su misma comuna (S/N): ")

t = cant_mas * v_mas
if t >= 15000:
    print(f'El envio es gratis. El valor de las mascarillas es: {t}.')
elif destino_env == "S" or destino_env == "s":
    print(f'El envio es de $1.000 y el total a pagar es: {t+1000}')
elif destino_env == "N" or destino_env == "n":
    print(f'El envio es de $2.000 y el total a pagar es: {t+2000}')
else:
    print(f'El envio es de $3.000 y el total a pagar es: {t+2000}')
    
# Ejercicio 2: Conversor.

def dolares_a_pesos(cantidad):
    valor_dolar = 800  # Valor aproximado del dólar en pesos chilenos
    resultado = cantidad * valor_dolar
    return resultado

def uf_a_pesos(cantidad):
    valor_uf = 30000   # Valor aproximado de la UF en pesos chilenos
    resultado = cantidad * valor_uf
    return resultado

def utm_a_pesos(cantidad):
    valor_utm = 50000  # Valor aproximado de la UTM en pesos chilenos
    resultado = cantidad * valor_utm
    return resultado

cantidad = float(input("Ingrese la cantidad a convertir: "))
unidad_origen = input("Ingrese la unidad de origen (dólares/UF/UTM): ")

if unidad_origen == "dólares":
    resultado = dolares_a_pesos(cantidad)
    unidad_destino = "pesos chilenos"
elif unidad_origen == "UF":
    resultado = uf_a_pesos(cantidad)
    unidad_destino = "pesos chilenos"
elif unidad_origen == "UTM":
    resultado = utm_a_pesos(cantidad)
    unidad_destino = "pesos chilenos"
else:
    print("Unidad de origen no válida")
    exit()

print(str(cantidad) + " " + unidad_origen + " equivalen a " + str(resultado) + " " + unidad_destino)


# Ejercicio 3: Menú


cant_chu = 0
cant_com = 0
cant_veg = 0
cant_barr = 0
t_chu = 0
t_com = 0
t_veg = 0
t_luc = 0
total = 0
while True:
    print(''' 
          1) Churrasco: $1.500
          2) Completo: $1.000
          3) Vegetariano: $2.000
          4) Barros luco: $3.000
          5) Salir / Total.
          
          ''')
    cant = int(input("Ingrese opción a llevar: "))
    if cant == 1:
        cant_chu = int(input("Ingrese cantidad de churrasco(s) a llevar: "))
        t_chu = 1500 * cant_chu
        total += t_chu
    elif cant == 2:
        cant_com = int(input("Ingrese cantidad de completo(s) a llevar: "))
        t_com = 1000 * cant_com
        total += t_com
    elif cant == 3:
        cant_veg = int(input("Ingrese cantidad de vegetariano(s) a llevar: "))
        t_veg = 2000 * cant_veg
        total += t_veg
    elif cant == 4:
        cant_barr = int(input("Ingrese cantidad de barros luco(s) a llevar: "))
        t_luc = 3000 * cant_barr
    elif cant == 5:
        print("### Sumario ###")
        print("Churrasco(s): ", cant_chu, "total: $", t_chu)
        print("Completo(s): ", cant_com, "total: $", t_com)
        print("Vegetariano(s): ", cant_veg, "total: $", t_veg)
        print("Barros luco(s): ", cant_barr, "total: $",t_luc)
        print("Total a pagar: ", total)
        break