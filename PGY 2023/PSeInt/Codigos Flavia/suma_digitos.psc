Algoritmo suma_digitos
	Definir num, suma, i Como Entero
	i=0;
	suma=0;
	Escribir "ingrese un numero";
	Leer num;
	Mientras num > 0 Hacer
		suma = suma + num mod 10; //num mod 10 devuelve el �ltimo d�gito
		num=trunc(num/10);
		i=i+1;
	FinMientras
	Escribir "la cantidad de d�gitos es: ",i, " y la suma es: ", suma;
	
FinAlgoritmo
