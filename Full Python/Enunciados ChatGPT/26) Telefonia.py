nombre = input("Nombre y apellido: ")
dia = input("Día de la llamada (en minúscula): ")
inicio_hora = int(input("Inicio de la llamada (hora de 0 a 23, valor entero): "))
inicio_minuto = int(input("Inicio de la llamada (minutos de 0 a 59, valor entero): "))
duracion_minutos = int(input("Duración de la llamada (minutos, valor entero): "))
duracion_segundos = int(input("Duración de la llamada (segundos, valor entero): "))

fraccion_minuto = duracion_segundos / 60
duracion_total_minutos = duracion_minutos + fraccion_minuto
costo = 0

if duracion_total_minutos <= 5:
    costo = duracion_total_minutos * 150
elif duracion_total_minutos <= 8:
    costo = 5 * 150 + (duracion_total_minutos - 5) * 95
elif duracion_total_minutos <= 10:
    costo = 5 * 150 + 3 * 95 + (duracion_total_minutos - 8) * 70
else:
    costo = 5 * 150 + 3 * 95 + 2 * 70 + (duracion_total_minutos - 10) * 50


if dia == "domingo":
    impuesto = costo * 0.03
elif inicio_hora >= 5 and inicio_hora < 12:
    impuesto = costo * 0.15
else:
    impuesto = costo * 0.1

costo_total = costo + impuesto


print("Estimado(a)", nombre + ":", "su llamada de", duracion_minutos, "minutos y", duracion_segundos, "segundos, realizada el día", dia, "a las", inicio_hora, ":", inicio_minuto, "tiene un costo de $", round(costo, 2), "más un impuesto de $", round(impuesto, 2), "lo que hace un total a pagar de: $", round(costo_total, 2))