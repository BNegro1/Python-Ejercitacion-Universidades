Algoritmo numero_magico
	
	Definir num, suma, mult Como Entero
	mult=1;
	suma=0;
	Escribir "ingrese un numero";
	Leer num;
	Mientras num > 0 Hacer
		suma = suma + num mod 10; //num mod 10 devuelve el último dígito
		mult = mult * num mod 10;
		num=trunc(num/10);
	FinMientras
	Si suma == mult Entonces
		Escribir "El número ingresado es mágico";
	sino 
		Escribir "El número ingresado no es mágico";
	FinSi
	
FinAlgoritmo
