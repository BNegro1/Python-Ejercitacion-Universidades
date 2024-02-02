Proceso factorial_de_nuevo
	Definir num, i, factorial, calculo Como Entero;
	factorial = 1;
	Escribir "ingresar un número a calcular su factorial";
	leer num;
	
	Para i=num  Hasta 1 con paso -1  Hacer
		factorial = factorial * i;
		//1
		//1*5 = 5
		//5*4=20
		//20*3=60
		//60*2=120
		//120*1=120
		
	FinPara
	EScribir factorial;
	
FinProceso
