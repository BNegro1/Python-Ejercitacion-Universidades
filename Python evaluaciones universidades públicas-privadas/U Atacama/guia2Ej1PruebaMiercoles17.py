charPlato = 0
salPlato = 0
lomoPlato = 0
tot = 0
c = 0
while True:
        print(''' 
                        Menú de ventas
            1) Registrar platos.
            2) Imprimir venta.
            3) Salir.
            
            ''')
        try:
            op = int(input("Ingrese opción: ")) 
            try:
                if op == 1:
                    while True:
                        print(''' 
                                        Platos
                            1) Charquican con huevo frito
                            2) Salteado de verduras con fideos
                            3) Lomo a lo pobre.
                            4) Volver al menú principal.
                                ''')
                        op2 = int(input("Ingrese una opción: "))
                        try:
                            if op2 == 1:
                                charPlato = int(input("Ingrese cantidad de platos: "))
                                tot = tot + (charPlato * 4500)
                            elif op2 == 2:
                                salPlato = int(input("Ingrese cantidad de platos: "))
                                tot = tot + (salPlato * 4500)                
                            elif op2 == 3:
                                lomoPlato = int(input("Ingrese cantidad de platos: "))
                                tot = tot + (lomoPlato * 4500)        
                            elif op2 == 4:
                                print("Volviendo al menú principal...")
                                break
                        except:
                            print("Ingrese una opción valida para el segundo menú.")
                elif op == 2:
                    print("Total de ventas")
                    print(f"Cantidad de charquican con huevo frito: {charPlato}")
                    print(f"Cantidad de charquican con huevo frito: {salPlato}") 
                    print(f"Cantidad de charquican con huevo frito: {lomoPlato}")              
                    print(f"Total a pagar: {tot}")        
                    pago = int(input("Ingrese total a pagar: "))
                    if pago < tot:
                        print("Ingrese un monto mayor o igual al total a pagar.")
                    elif pago >= tot:
                        print("Compra realizada correctamente. Vuelto:",pago-tot)
                elif op == 3:
                    print("Ha salido correctamente del programa.")
                    break
            except:
                print("Ingrese una opción valida.")
        except:
            print("Ingrese una opción valida.")