Proceso multiplos_de_5 //3.	Imprimir contar y sumar los m�ltiplos de 5 que hay entre 1 y un n�mero que el usuario introduce por teclado.
	Definir i, suma, num, cont Como Entero;
	suma=0;
	cont=0;
	Escribir "ingrese un n�mero";
	Leer num;
	
	Para i=1 Hasta num Hacer
		Si i mod 5 == 0 Entonces
			EScribir i;
			suma=suma+i;
			cont=cont+1;
			
		FinSi
	FinPara
	Escribir "la cantidad de m�ltiplos de 5 entre 1 y ",num, " es: ",cont;
	Escribir "y la suma es de: ", suma;
FinProceso
