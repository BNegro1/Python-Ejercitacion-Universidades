Algoritmo tabla_mutiplicar
	Definir num Como Entero;
	Escribir "Ingrese un n�mero positivo: ";
	leer num;
	si num > 0 Entonces
		Para i = 1 Hasta 10 Con Paso 1 Hacer
			Escribir num, "*", i, "=", num*i;
		FinPara
	SiNo
		Escribir "El n�mero es negativo o igual a cero";
	FinSi
	
FinAlgoritmo
