Proceso sumaDeCuadrados //4.	Calcular la suma de los cuadrados de los números pares entre 0 y 200
	Definir i, suma Como Entero;
	suma=0;
	
	Para i=0 Hasta 200 Hacer
		Si i mod 2 == 0 Entonces
			//Escribir i,"-", i^2;
			suma = suma + i^2;
			//Escribir suma;
			
		FinSi
	FinPara
	Escribir "La suma de los cuadrados de los números pares entre 0 y 200 es: ", suma;
FinProceso
