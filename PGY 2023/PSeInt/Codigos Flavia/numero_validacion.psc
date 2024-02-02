Proceso numero_validacion //9.	Introducir un número por teclado entre 500 y 5000. Validar que sea así. 
	//Si es mayor que 500 y menor que 700, adicionarle el 50% y mostrarlo. 
	//Si es el número es mayor que 700 y menor que 1000, sumarle el 25% y mostrarlo. 
	//Si el número es mayor o igual a 1000, pero menor que 3000, entonces sumarle el 15% y mostrarlo. 
	//Si el número es igual o mayor que 3000, pero menor que 4000, entonces sumarle el 5% y mostrarlo. 
	//Y si el número es igual o mayor que 4000 y menor o igual que 5000,entonces restarle el 5% y mostrarlo.
	Definir num Como Entero;
	
	Repetir
		Escribir "ingrese un número entre 500 y 5000";
		leer num;
	Hasta Que num >= 500 y num <= 5000
	
	Si num >= 500 y num<700 Entonces
		Escribir num*1.5;
	SiNo
		si num >= 700 y num < 1000 Entonces
			Escribir num*1.25;
		SiNo
			si num >=1000 y num < 3000 Entonces
				Escribir num*1.15;
			SiNo
				si num >=3000 y num<4000 Entonces
					EScribir num*1.05;
				SiNo
					Escribir num*0.95;
				FinSi
				
			FinSi
		FinSi
	FinSi
	
FinProceso
