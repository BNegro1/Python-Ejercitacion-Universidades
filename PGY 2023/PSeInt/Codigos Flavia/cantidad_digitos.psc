Algoritmo cantidad_digitos
	Definir num, suma, i Como Entero
	i=0;
	Escribir "ingrese un numero";
	Leer num;
	Mientras num > 0 Hacer
		num=trunc(num/10)
		i=i+1
	FinMientras
	Escribir "la cantidad de dígitos es: ",i;
	
FinAlgoritmo
