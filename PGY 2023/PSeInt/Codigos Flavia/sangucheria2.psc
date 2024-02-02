Proceso sangucheria2
	Definir n_opcion, total, total_turno Como Entero;
	Definir letra_opcion Como Caracter;
	total=0;
	total_turno=0;
	n_opcion=1;
	
	Repetir //ciclo que muestra menu a/b/c hasta que se ingrese c (salida)
		Escribir "Elija una opción:";
		Escribir "a) Realizar Venta";
		Escribir "b) Cerrar Turno";
		Escribir "c) Salir";
		Leer letra_opcion;
		Escribir letra_opcion;
		
		Si letra_opcion == "a" Entonces; //ciclo si se ingresa opcion a (venta)
			Repetir
				Escribir "Elija una opción";
				Escribir "1.DuocChoripan $1200";
				Escribir "2. DuocItaliano $1500";
				Escribir "3.DuocVegano $2000";
				Escribir "4.Salir";
				Leer n_opcion;
				Si n_opcion == 1 Entonces;
					total=total + 1200;
					Escribir "se ha sumado un DuocChoripan";
				SiNo
					si n_opcion == 2 Entonces
						total=total+1500;
						Escribir "se ha sumado un DuocItaliano";
					SiNo
						si n_opcion == 3 Entonces;
							total = total + 2000;
							Escribir "se ha sumado un DuocVegano";
						sino
							si n_opcion == 4 Entonces;
								Escribir "el total a pagar es: ", total;
							SiNo
								Escribir "ingrese una opción válida";
								
							FinSi
						FinSi
						
					FinSi
					
				FinSi
				
			
			Hasta Que n_opcion == 4
			n_opcion=1; //reinicio de opcion para que siga entrando al ciclo
			total_turno=total+total_turno; //calculo de la suma de las ventas por turno
			total=0; //reiniciar el total a cobrar al siguiente cliente
			
		SiNo
			si letra_opcion == "b" Entonces;//ciclo para cerrar el turno de la caja y mostrar el monto recaudado
				Escribir "La recaudación acumulada en la caja es de: ", total_turno;
				total_turno = 0; //reiniciar el monto en la caja
				
			FinSi
			
		FinSi
		
	Hasta Que letra_opcion == "c"; 
	
FinProceso
