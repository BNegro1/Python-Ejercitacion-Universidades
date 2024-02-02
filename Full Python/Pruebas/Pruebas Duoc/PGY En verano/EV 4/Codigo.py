# Se crean las listas
asientos = []
pasajeros = []
ruts = []
# Se definen las variables
precio_normal = 14900
precio_vip = 24000
# Ciclo para generar los asientos
for x in range(1, 41):
    asientos.append(x)
# Menú principal
while True:
    print('''
                        Ferroviaria
                        
        1) Ver asientos disponibles.
        2) Comprar asiento.
        3) Anular viaje.
        4) Modificar por RUT
        5) Salir.                        
          ''')
    op = int(input("Ingrese una opción: "))
    if op == 1:
        # Crear dos sub-listas para los números impares y pares
        puestos_impares = [str(x) for x in range(1, 41, 2)]
        puestos_pares = [str(x) for x in range(2, 42, 2)]

        # Crear listas para cada línea de números
        linea1 = ' '.join(puestos_impares[:10]) + '  || ' + ' '.join(puestos_impares[10:])
        linea2 = ' '.join(puestos_pares[:10]) + ' || ' + ' '.join(puestos_pares[10:])

        resultado = [linea1, linea2]

        # Imprimir el resultado
        print('\n'.join(resultado))
    elif op == 2:
        rut = (input("Ingrese rut (sin digito verificador): "))
        if len(rut) == 8 and rut.isdigit():
            ruts.append(int(rut))
        print(ruts)