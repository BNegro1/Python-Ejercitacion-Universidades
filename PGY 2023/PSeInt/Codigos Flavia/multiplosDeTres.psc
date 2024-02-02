Proceso multiplosDeTres //1.	Hacer un programa que imprima y cuente los múltiplos de 3 que hay entre 1 y 100
	Definir i, cont Como Entero;
	cont=0;
	
	Para i=1 Hasta 100 Hacer
		si i mod 3 == 0 Entonces
			Escribir i;
			cont=cont+1;
			
		FinSi
	FinPara
	Escribir "la cantidad de múltiplos de 3 entre 1 y 100 es: ",cont;
FinProceso
