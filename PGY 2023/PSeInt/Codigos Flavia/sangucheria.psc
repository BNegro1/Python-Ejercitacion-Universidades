Algoritmo sangucheria
	Definir n_opcion Como Entero;
	Definir letra_opcion Como Caracter;
	
	Repetir
		Escribir "Elija una opción:";
		Escribir "a) Realizar Venta";
		Escribir "b) Cerrar Turno";
		Escribir "c) Salir";
		Leer letra_opcion;
		
		Si letra_opcion == "a" Entonces
			
			Escribir "Elija una opción";
			Escribir "1.DuocChoripan $1200";
			Escribir "2. DuocItaliano $1500";
			Escribir "3.DuocVegano $2000";
			Escribir "4.Salir";
		sino 
			Si letra_opcion == "b" Entonces
				
			FinSi
		FinSi
		
	Hasta Que letra_opcion == "a" o letra_opcion == "b" o letra_opcion == "c";
	
	
	
FinAlgoritmo
