Proceso fibonacci2 //partiendo desde 1
	Definir i, num, suma1, suma2,suma3 Como Entero;
	Escribir "Ingrese un número";
	Leer num;
	suma1 = 1;
	suma2 = 1;
	Para i=1 Hasta num Hacer
		Escribir suma1;
		suma3=suma1+suma2;
		suma1=suma2;
		suma2 = suma3;
	FinPara
	
FinProceso
