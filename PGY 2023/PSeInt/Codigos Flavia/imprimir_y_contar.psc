Proceso imprimir_y_contar //7.	Imprimir y contar los n�meros que existen ente dos n�meros ingresados por teclado, excepto los m�ltiplos de 2 y de 5. Por final de programa mostrar la suma de los m�ltiplos de 2 y de 5.
	Definir i, num1, num2, cont,  num_mayor, num_menor, suma Como Entero;
	cont=0;
	suma=0;
	EScribir "Ingrese dos n�meros";
	Leer num1, num2;
	
	Si num1 > num2 Entonces
		num_mayor = num1;
		num_menor = num2;
	SiNo
		num_mayor = num2;
		num_menor = num1;
		
	FinSi
	
	Para i=num_menor+1 Hasta  num_mayor-1 Hacer
		Si i mod 2 == 0 o i mod 5 == 0 Entonces
			suma=suma+i;	
		SiNo
			Escribir i;
			cont=cont+1;
		FinSi
		
	FinPara
	
	Escribir "la cantidad de n�meros que existen entre ",num_menor," y ",num_mayor," exceptuando los m�ltiplos de 2 y 5 es: ", cont;
	Escribir "la suma de los m�ltiplos de 2 y 5 entre ",num_menor," y ",num_mayor," es: ", suma;
	
	
	
FinProceso
