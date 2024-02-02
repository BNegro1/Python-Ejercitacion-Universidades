Algoritmo serviciomilitar
	Definir edad Como Entero;
	Definir sexo Como Caracter;
	
	Escribir "Ingrese su sexo(F/M): ";
	Leer sexo;
	Escribir "Ingrese su edad: ";
	Leer edad;
	si edad >= 18 y edad < 25 y sexo=="M" Entonces;
		Escribir "Usted debe hacer el servicio militar";
	SiNo
		Escribir "Usted no debe hacer el servicio militar";
		
	FinSi
FinAlgoritmo
