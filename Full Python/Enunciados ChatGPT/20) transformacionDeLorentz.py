#Transformación de Lorentz: Escribir un programa en Python que implemente 
#la transformación de Lorentz y 
#muestre cómo los intervalos de tiempo y las distancias 
#varían en diferentes sistemas inerciales.

c = 3 * (10**8) # Velocidad de la luz en metros por segundo

def transformacion_lorentz(v, t, x):
    t_prima = (t - (v * x) / c**2) / (1 - (v**2 / c**2))**0.5
    x_prima = (x - v * t) / (1 - (v**2 / c**2))**0.5
    print(f'Tiempo dilatado: {t_prima} [S]')
    print(f'Distancia contraída: {x_prima} [M]')
    return t_prima, x_prima

v = float(input("Ingrese la velocidad del objeto en movimiento en metros por segundo: "))
t = float(input("Ingrese el tiempo medido en un sistema inercial (reposo): "))
x = float(input("Ingrese la distancia medida en un sistema inercial (reposo): "))
transformacion_lorentz(v, t, x)