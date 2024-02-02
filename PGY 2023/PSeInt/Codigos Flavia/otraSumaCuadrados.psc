Proceso otraSumaCuadrados //5.	Hacer un programa que permita que el usuario introduzca por teclado un número menor a 500. Imprimir la suma de los cuadrados de los números que están separados entre sí por 4 posiciones.
	Definir i, num, suma Como Entero;
	suma=0;
	
	Repetir
		Escribir "ingrese un número";
		Leer num;
	Hasta Que num < 500 
	PAra i=0  Hasta num con paso 4 hacer
		escribir i,"-",i^2;
		suma=suma+i^2;
	FinPara
	
	Escribir "la suma de los cuadrados de los números separados entre sí por 4 posiciones comprendidos entre 0 y ",num," es: ", suma;
	
	
FinProceso
