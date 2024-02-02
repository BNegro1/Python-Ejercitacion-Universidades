Proceso pitagoras
	Definir lado1, lado2, lado3 Como Entero;
	
	Repetir
		Escribir "ingrese los lados de un triángulo: ";
		leer lado1, lado2, lado3;
	Hasta Que lado1 >0 y lado2>0 y lado3>0
	
	si lado1^2 == lado2^2 + lado3^2 Entonces
		Escribir "el triángulo cumple con el teorema de Pitágoras";
	sino 
		si lado2^2==lado1^2+lado3^2 Entonces
			Escribir "el triángulo cumple con el teorema de Pitágoras";
		sino 
			si lado3^2==lado1^2+lado2^2 Entonces
				Escribir "el triángulo cumple con el teorema de Pitágoras";
			SiNo
				Escribir "el triángulo  no cumple con el teorema de Pitágoras";
						
			FinSi
		FinSi
		
	FinSi
	
	
FinProceso
