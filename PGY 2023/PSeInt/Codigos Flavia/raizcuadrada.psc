Proceso raizcuadrada
	//hacer un algoritmo que calcule la raiz cuadrada de un  numero mediante multiplicaciones
	//asumir que usuario ingresa numeros con raiz cuadrada exacta
	Definir num, multiplicacion, i Como Real;
	i=1;
	multiplicacion=1;
	Escribir "ingrese el número a calcular su raiz cuadrada";
	leer num;
	
	Repetir
		multiplicacion = i*i;
		i=i+1;
	Hasta Que multiplicacion = num
	
	Escribir "la raiz es: ", i-1;
	
FinProceso
