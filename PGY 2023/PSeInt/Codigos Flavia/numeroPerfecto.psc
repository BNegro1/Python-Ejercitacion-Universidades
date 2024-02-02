Proceso numeroPerfecto //ej de numeros perfectos: 6, 28, 496
	definir num, i, suma Como Entero; //numero perfecto es aquel que es igual a la suma de sus divisores
	suma=0;
	Repetir
		Escribir "Ingrese un número entre 1 y 30";
		Leer num;
	Hasta Que num <= 30 y num > 0
	Para i=1 Hasta num-1 Hacer
		Si num mod i == 0 Entonces
			suma=suma+i;
		FinSi
	FinPara
	Si num==suma Entonces
		Escribir "el número ",num," es perfecto";
	SiNo
		Escribir "el número ",num," no es perfecto";
	FinSi
	
FinProceso
