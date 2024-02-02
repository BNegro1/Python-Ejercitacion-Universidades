Algoritmo sumar //sumar 5 numeros utilizando sentencia Mientras
	Definir num, i, suma Como Entero;
	suma = 0;
	i=1
	Mientras i<=5 Hacer
		Escribir "Ingresar número ",i," :";
		Leer num;
		suma=suma+num;
		i=i+1; //cuidado de no olvidar esto o queda un bucle infinito
	FinMientras
	Escribir "La suma de los cinco números es: ", suma;
	
FinAlgoritmo
