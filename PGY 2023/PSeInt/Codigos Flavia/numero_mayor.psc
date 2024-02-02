Proceso numero_mayor
	Definir num1, num2, num3, mayor Como Entero;
	Escribir "Ingrese los tres números";
	Leer num1;
	LEer num2;
	Leer num3;
	
	Si num1>num2 Entonces		
		Si num1 > num3 Entonces
			mayor = num1;
		SiNo
			mayor=num3;
		FinSi
	sino 
		si num2>num3 Entonces
			mayor=num2;
		SiNo
			mayor=num3;
		FinSi
	FinSi
	
	Escribir "el número mayor es: ", mayor;
FinProceso
