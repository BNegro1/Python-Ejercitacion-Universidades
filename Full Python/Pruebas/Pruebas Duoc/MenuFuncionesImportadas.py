import numpy as np
from datetime import date
from functions import valida_rut, render_asientos_usados, asiento_reservado, reserva_asiento, reserva_rut_bd, reserva_rut, listar_rut_ordenado

total_entrada_platinum = 0
total_entrada_gold = 0
total_entrada_silver = 0

acc_entrada_platinum = 0
acc_entrada_gold = 0
acc_entrada_silver = 0

valor_platinum = int(120000)
valor_gold = int(80000)
valor_silver = int(50000)

users_bd = []
asientos_concierto = np.arange(1, 101, 1)

etapa_menu = True

while etapa_menu:
    try:
        respuesta_menu = int(input(
            '*** Bienvenido a Creativos.cl - "Michel Jam" ***\n 1.- Comprar Entradas\n 2.- Mostrar ubicaciones disponibles\n 3.- Ver listado de asistentes\n 4.- Mostrar ganancias totales\n 5.- Salir\n'))
    except:
        print('Ups! Opción inválida, vuelva a intentarlo.')
    else:
        if respuesta_menu == 1:
            user = []
            count_tickets = 0
            add_entrada = True
            while add_entrada:
                try:
                    cant_entradas = int(input('Estimado, a continuación ingrese la cantidad de entradas a comprar, puede comprar máximo 3 por persona ->\n Considere los siguientes precios para las Entradas: \n • Platinum $120.000 (Asientos del 1 al 20)\n • Gold $80.000 (Asientos del 21 al 50) \n • Silver $50.000 (Asientos del 51 al 100)\n'))

                    count_tickets = cant_entradas

                    if cant_entradas >= 1 and cant_entradas <= 3:
                        concierto_matriz = render_asientos_usados(asientos_concierto).reshape(10, 10)
                        pantalla_cliente = f'\t ******* ESCENARIO ******* \n {concierto_matriz}\n'
                        print(pantalla_cliente)

                        add_entrada = False
                    else:
                        print('Solo puedes ingresar un máximo de 3 entradas y un mínimo de 1!\n')
                except:
                    print('Opción inválido, Solo puede ingresar valores validos. Por Favor, vuelva a intentarlo!\n')
                
            add_asientos = True
            while add_asientos:
                asientos_reservado = []
                valor_asiento = []
                rut_usuarios = []
                try:

                    while count_tickets > len(asientos_reservado):
                        numero_reserva = int(input('Ingrese el número de asiento para reservar: -> '))
                        ocupado = asiento_reservado(asientos_concierto, numero_reserva)

                        if ocupado:
                            asientos_reservado.append(numero_reserva)
                           

                            if numero_reserva >= 1 and numero_reserva <= 20:
                                acc_entrada_platinum = acc_entrada_platinum + 1
                                total_entrada_platinum = total_entrada_platinum + valor_platinum
                                valor_asiento.append(valor_platinum)

                            elif numero_reserva >= 21 and numero_reserva <= 50:
                                acc_entrada_gold = acc_entrada_gold + 1
                                total_entrada_gold = total_entrada_gold + valor_gold
                                valor_asiento.append(valor_gold)

                            elif numero_reserva >= 51 and numero_reserva <= 100:
                                acc_entrada_silver = acc_entrada_silver + 1
                                total_entrada_silver = total_entrada_silver + valor_silver
                                valor_asiento.append(valor_silver)
                            
                            add_rut = True
                            while add_rut:
                                try:

                                    rut_usuario = input(f'Debes registrar el Rut de la entrada para el asiento: {numero_reserva} (Ej: 12345678-9) -> ')
                                    new = rut_usuario.split('-')
                                    formated_rut = new[0]

                                    rut_validado = valida_rut(rut_usuario)


                                    try:
                                        rut_registrado_bd = reserva_rut_bd(users_bd, int(formated_rut))
                                        if rut_registrado_bd:
                                            print('Rut tiene registro y reserva de entrada! Ingrese un Nuevo Rut para reservar :)\n')
                                        else:
                                            rut_registrado = reserva_rut(rut_usuarios, int(formated_rut))
                                            if rut_registrado:
                                                print('Rut agregado recientemente. Las reservas son unitarias e instransferibles!\n')
                                            else:
                                                if rut_validado:
                                                    rut_usuarios.append(int(formated_rut))
                                                    reserva_asiento(asientos_concierto, numero_reserva)
                                                    print('Rut Válido! Operación realizada Correctamente :)\n')
                                                    add_rut = False
                                                else:
                                                    print('RUT ingresado no es válido. Revise nuevamente el digito verificador!')
                                    except:
                                        print('Error con registro de RUT! \n')
                                except:
                                    print('Ha ocurrido un Error al registrar tu RUT. Intenta nuevamente :)')
                                
                        else:
                            print('Asiento reservado!. Elija otro que esté disponible.')
                        
                    concierto_matriz = render_asientos_usados(asientos_concierto).reshape(10, 10)
                    pantalla_cliente = f'\t******* ESCENARIO ******* \n {concierto_matriz}\n'
                    user.append(rut_usuarios)
                    user.append(asientos_reservado)
                    user.append(valor_asiento)
                    print(f'{pantalla_cliente}\n Asientos reservados con éxito!\n')
               
                    add_asientos = False
                except:
                    print('Valores ingresados No Válidos! Intente nuevamente :(\n')

            add_nombre = True
            while add_nombre:
                try:
                    respuesta_nombre_afiliado = input('Ingrese nombre del titular: ->\n')
                    if respuesta_nombre_afiliado.isalpha():
                        if len(respuesta_nombre_afiliado) > 2:
                            user.append(respuesta_nombre_afiliado)
                            add_nombre = False
                        else:
                            print('Debe ingresar un Nombre válido.\n')
                    else:
                        print('Debe ingresar un Nombre (letras)!\n')
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!')

            add_apellido = True
            while add_apellido:
                try:
                    respuesta_apellido_afiliado = input('Ingrese su apellido Paterno ->\n')
                    if respuesta_apellido_afiliado.isalpha():
                        if len(respuesta_apellido_afiliado) > 2:
                            user.append(respuesta_apellido_afiliado)
                            add_apellido = False
                        else:
                            print('Debe ingresar un Apellido válido.\n')
                    else:
                        print('Debe ingresar un Apellido (letras)!\n')
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!')
            print('Registro completo exitoso!\n')
            users_bd.append(user)
        
        elif respuesta_menu == 2:
            print('Los asientos reservados están marcados con X: ->\n')
            concierto_matriz = render_asientos_usados(asientos_concierto).reshape(10, 10)
            pantalla_cliente = f'\t******* ESCENARIO ******* \n {concierto_matriz}\n'

            print(pantalla_cliente)

        elif respuesta_menu == 3:
            if len(users_bd) > 0:
                listar = listar_rut_ordenado(users_bd)
                print(f'Los RUT de los asistentes son: (Ordenados) ->\n')
                for index, r in enumerate(listar):
                    print(f'{index + 1} - {r}\n')
            else:
                print('La base de datos se encuentra vacía! Debes registrar al menos una reserva.\n')
        
        elif respuesta_menu == 4:
            total_platinum = acc_entrada_platinum * valor_platinum
            total_gold = acc_entrada_gold * valor_gold
            total_silver = acc_entrada_silver * valor_silver

            print(f'\t ***** Ganancias Totales ***** \n Entradas Platinum ${valor_platinum}-> Cantidad: {acc_entrada_platinum} - Total Recaudado: ${total_platinum}\n Entradas Gold ${valor_gold} -> Cantidad: {acc_entrada_gold} - Total Recaudado: ${total_gold}\n Entradas Silver ${valor_silver} -> Cantidad: {acc_entrada_silver} - Total Recaudado: ${total_silver}\n\n Total Ganado: ${total_platinum + total_gold + total_silver}')

        elif respuesta_menu == 5:
            fecha_registro = date.today()
            fecha_formated = fecha_registro.strftime("%d/%m/%Y")
            print(f'Cerrando Sesión...\n Desarrollado por Matías Espinoza® - {fecha_formated}\n')
            etapa_menu = False

        else:
            print('Opción inválida, intente nuevamente o contacte al administrador.')