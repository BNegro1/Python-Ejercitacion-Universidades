Proceso ingresarNumeros
	Definir num, num_pares, suma_impares, suma_negativos, cont_negativos, cont_positivos, i Como Entero;
	num_pares=0;
	suma_impares=0;
	suma_negativos=0;
	cont_negativos=0;
	cont_positivos=0;
	Para i=1 Hasta 10 Hacer
		Escribir "ingrese un número";
		leer num;
		Si num mod 2 == 0 Entonces
			num_pares = num_pares + 1;
		sino 
			suma_impares = suma_impares + num;
		FinSi
		Si num >= 0 Entonces
			cont_positivos = cont_positivos + 1;
		SiNo
			suma_negativos=suma_negativos+num;
			cont_negativos=cont_negativos+1;
		FinSi
	FinPara
	
	Escribir "la cantidad de numeros pares es: ", num_pares;
	Escribir "la suma de los números impares es: ", suma_impares;
	Escribir  "el promedio de los números negativos es igual a: ", suma_negativos/cont_negativos;
	Escribir "la cantidad de números positivos es: ", cont_positivos;
FinProceso
