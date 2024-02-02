Proceso factorial
	Definir i, num, factor Como Entero;
	factor = 1;
	Escribir "Ingresar un número";
	Leer num;
	Para i=1 Hasta num Hacer
		factor=factor*i;
	FinPara
	Escribir "El factorial de ", num, " es: ", factor;
	
FinProceso
