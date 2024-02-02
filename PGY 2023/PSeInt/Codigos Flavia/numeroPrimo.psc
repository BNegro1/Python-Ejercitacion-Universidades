Algoritmo numeroPrimo
	Definir num Como Real
	Definir cont_divisores Como Entero
	cont_divisores=0;
	Escribir "Ingrese un número positivo";
	Leer num;
	Para i=1 Hasta num Hacer
		si num mod i == 0
			cont_divisores=cont_divisores+1;
			
		FinSi
	FinPara
	Si cont_divisores == 2
		Escribir "el número es primo";
	SiNo
		Escribir "el número no es primo";
	FinSi
	
	
FinAlgoritmo
