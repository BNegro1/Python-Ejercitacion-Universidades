Proceso numeros_naturales //6.	Hacer un programa que permita introducir dos números distintos por teclado. Imprimir los números naturales que hay entre ellos comenzando desde el más chico, contar cuántos hay e imprimir los pares que existan.
	// lo hice ]num_menor, num_mayor[
	Definir i, num1, num2, num_mayor, num_menor, cont_par, cont_natural Como Entero;
	cont_par=0;
	cont_natural=0;
	
	Escribir "ingrese dos números";
	Leer num1, num2;
	
	Si num1 > num2 Entonces
		num_mayor = num1;
		num_menor = num2;
	SiNo
		num_mayor = num2;
		num_menor = num1;
		
	FinSi
	Escribir "numeros naturales entre ",num_menor," y ",num_mayor,": ";
	Para i=num_menor+1 Hasta num_mayor-1 Hacer
		Escribir i;
		cont_natural=cont_natural + 1;
		Si i mod 2 ==0 Entonces
			cont_par=cont_par+1;
			
		FinSi
	FinPara
	Escribir "la cantidad de numeros naturales entre ",num_menor," y ", num_mayor," es: ", cont_natural;
	Escribir "la cantidad de numeros pares entre ",num_menor," y ", num_mayor," es: ", cont_par;
FinProceso
