Proceso camisas_descuento
	Definir total_pagar, cant_camisas, precio Como Real;
	Escribir "ingrese la cantidad de camisas a comprar";
	Leer cant_camisas;
	Escribir "ingrese precio de las camisas";
	Leer precio;
	
	Si cant_camisas >=3 Entonces;
		total_pagar = precio - (precio*0.2);
	
	SiNo 
		total_pagar = precio - (precio*0.1);
				
	FinSi
	Escribir "El total a pagar es: ",total_pagar;
FinProceso
