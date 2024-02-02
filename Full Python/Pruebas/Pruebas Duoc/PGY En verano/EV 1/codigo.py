t = []
while True:
    print(''' 
                Bienvenido a McBurguer
        1) Encargar.
        2) Pagar.
        3) Salir y cotizar.
    
          ''')
    op = int(input("Ingrese opción: "))
    if op == 1:
        print('''
            Sandwiches               Solo / Combo
            
        - Italiano        |        $2.000 / $3.500       
        - Dinamico        |        $2.200 / $3.600
        - A lo pobre      |        $2.500 / $3.900
               
              ''')
        t_san = input("Ingrese tipo de sandwich: ")
        tarifa = input("Ingrese tipo de tarifa (Solo/Combo): ")

        if t_san == 'Italiano' and tarifa == 'Solo':
            print("Sandiwch: Italiano | Tarifa: Solo")
            t.append(2000)
        elif t_san == 'Italiano' and tarifa == 'Combo':
            print("Sandiwch: Italiano | Tarifa: Combo")
            t.append(3500)
        elif t_san == 'Dinamico' and tarifa == 'Solo':
            print("Sandiwch: Dinamico | Tarifa: Solo")   
            t.append(2200)     
        elif t_san == 'Dinamico' and tarifa == 'Combo':
            print("Sandiwch: Dinamico | Tarifa: Combo")   
            t.append(3600)
        elif t_san == 'A lo pobre' and tarifa == 'Solo':
            print("Sandiwch: A lo pobre | Tarifa: Solo")
            t.append(2500)        
        elif t_san == 'A lo pobre' and tarifa == 'Combo':
            print("Sandiwch: A lo pobre | Tarifa: Combo")                              
            t.append(3900)
    elif op == 2:
        print("Total a pagar:", sum(t))
    elif op == 3:
        pago = int(input(f'Total a pagar: {sum(t)} ingrese monto: '))
        if pago >= sum(t):
            print("Gracias por comer en McBurguer.")
            break
        else:
            print("Ingrese pago correcto por favor.")
        