Algoritmo multiplicacion
	Definir i, num1, num2, suma Como Entero;
	suma=0;
	Escribir "Ingresar primer número a multiplicar";
	Leer num1;
	Escribir "Ingresar segundo número a multiplicar";
	Leer num2;
	Para i=1 Hasta num2 Hacer
		suma=num1+suma;
	FinPara
	Escribir num1, "*", num2, "=", suma;
FinAlgoritmo
