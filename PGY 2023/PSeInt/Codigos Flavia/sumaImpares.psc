Proceso sumaImpares //2.	Hacer un programa que calcule la suma de los números impares comprendidos entre 1 y 100.
	Definir i, suma como entero;
	suma=0;
	Para i=1 hasta 100 Hacer
		Si i mod 2 == 1 Entonces
			
			Escribir i;
			suma=suma+i;
			
		FinSi

	FinPara
	Escribir "la suma de los numeros impares comprendidos entre 1 y 100 es: ",suma;
FinProceso
