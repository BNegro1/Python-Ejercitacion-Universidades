Proceso pares_e_impares //8.	Introducir dos números diferentes por teclado, de forma tal que el segundo sea mayor que el primero. Averiguar cuántos son pares y mostrar, por final de programa, la suma de los impares.
	//supongo que cuantos pares e impares hay entre esos dos numeros
	Definir i, cont, suma, num1, num2 Como Entero;
	cont=0;
	suma=0;
	Repetir
		Escribir "ingrese dos números, primero el menor y luego el mayor";
		LEer num1, num2;
	Hasta Que num1 < num2
	
	
	Para i=num1+1 Hasta num2-1 Hacer
		Si i mod 2 == 0 Entonces
			cont=cont+1;
		SiNo
			suma=suma+i;
		
		FinSi
	FinPara
	EScribir "la cantidad de números pares entre ", num1, " y ", num2, " es: ",cont," y la suma de los impares entre ellos es de: ", suma;
FinProceso
