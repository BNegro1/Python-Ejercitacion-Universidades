Proceso otraSumaCuadrados //5.	Hacer un programa que permita que el usuario introduzca por teclado un n�mero menor a 500. Imprimir la suma de los cuadrados de los n�meros que est�n separados entre s� por 4 posiciones.
	Definir i, num, suma Como Entero;
	suma=0;
	
	Repetir
		Escribir "ingrese un n�mero";
		Leer num;
	Hasta Que num < 500 
	PAra i=0  Hasta num con paso 4 hacer
		escribir i,"-",i^2;
		suma=suma+i^2;
	FinPara
	
	Escribir "la suma de los cuadrados de los n�meros separados entre s� por 4 posiciones comprendidos entre 0 y ",num," es: ", suma;
	
	
FinProceso
