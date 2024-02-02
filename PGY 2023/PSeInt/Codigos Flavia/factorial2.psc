Proceso factorial2
	Definir i, num, fact Como Entero;
	fact = 1;
	Escribir "ingrese un numero entre 3 y 6: ";
	Leer num;
	si num > 2 y num < 7 Entonces
		PAra i=1 Hasta num Con Paso 1 Hacer
			fact = fact * i;
		FinPara
		Escribir "el factorial de ", num, " es: ", fact;
	SiNo
		Escribir "numero fuera de rango";
	FinSi
	
FinProceso
