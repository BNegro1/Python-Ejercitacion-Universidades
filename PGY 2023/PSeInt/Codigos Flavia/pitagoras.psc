Proceso pitagoras
	Definir lado1, lado2, lado3 Como Entero;
	
	Repetir
		Escribir "ingrese los lados de un tri�ngulo: ";
		leer lado1, lado2, lado3;
	Hasta Que lado1 >0 y lado2>0 y lado3>0
	
	si lado1^2 == lado2^2 + lado3^2 Entonces
		Escribir "el tri�ngulo cumple con el teorema de Pit�goras";
	sino 
		si lado2^2==lado1^2+lado3^2 Entonces
			Escribir "el tri�ngulo cumple con el teorema de Pit�goras";
		sino 
			si lado3^2==lado1^2+lado2^2 Entonces
				Escribir "el tri�ngulo cumple con el teorema de Pit�goras";
			SiNo
				Escribir "el tri�ngulo  no cumple con el teorema de Pit�goras";
						
			FinSi
		FinSi
		
	FinSi
	
	
FinProceso
