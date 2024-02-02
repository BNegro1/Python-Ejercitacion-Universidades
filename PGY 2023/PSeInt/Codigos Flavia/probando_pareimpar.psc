Proceso probando_pareimpar
	definir i, num como entero;
	
	escribir "ingrese num";
	leer num;
	
	Si num < 0 Entonces
		num= num*(-1);
	FinSi
	Si num mod 2 == 0 Entonces
		escribir "es par";
	SiNo
		si num mod 2 == 1 Entonces
			escribir "es impar";
		SiNo
			escribir "error";
		FinSi
	FinSi
	
FinProceso
