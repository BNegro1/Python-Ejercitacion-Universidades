Algoritmo tabla_mutiplicar
	Definir num Como Entero;
	Escribir "Ingrese un número positivo: ";
	leer num;
	si num > 0 Entonces
		Para i = 1 Hasta 10 Con Paso 1 Hacer
			Escribir num, "*", i, "=", num*i;
		FinPara
	SiNo
		Escribir "El número es negativo o igual a cero";
	FinSi
	
FinAlgoritmo
