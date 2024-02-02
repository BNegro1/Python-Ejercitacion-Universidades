Proceso calculadora //10.	Hacer un programa que admita que el usuario pueda ingresar dos números, 
	//y luego muestre el siguiente menú: SUMA, RESTA, PRODUCTO y COCIENTE. 
	//Para elegir qué operación efectuar, el usuario debe introducir las iniciales de cada operación, 
	//es decir S, R, P o C, luego de lo cual el programa mostrará el resultado obtenido. 
	//Permitir que el usuario pueda hacer tantas de estas operaciones como quiera, 
	//contestando con S(si) o N(no) a la pregunta: "¿sigue calculando?".
	definir suma, resta, producto, cociente, num1, num2 Como Real;
	definir opcion Como Caracter;
	
	Repetir
		Escribir "ingrese dos números";
		LEer num1, num2;
		Escribir "Elija una opción (S/R/P/C): ";
		Escribir "SUMA";
		Escribir "RESTA";
		Escribir "PRODUCTO";
		Escribir "COCIENTE";
		Leer opcion;
		
		Si opcion == "S" Entonces
			Escribir num1,"+",num2,"=", num1+num2;
		FinSi
		Si opcion == "R" Entonces
			Escribir num1,"-",num2,"=", num1-num2;
		FinSi
		Si opcion == "P" Entonces
			Escribir num1,"*",num2,"=", num1*num2;
		FinSi
		Si opcion == "C" Entonces
			Escribir num1,"/",num2,"=", num1/num2;
		FinSi
		Repetir 
			Escribir "¿Sigue calculando(S/N)?";
			leer opcion;
			Si opcion <> "S" y opcion <> "N" Entonces
				escribir "Por favor ingrese una opción válida";
			FinSi
		hasta que opcion == "S" o opcion == "N"
	hasta que opcion = "N"
	
	Escribir "Se cierra el programa";
	
	
	
	
	
	
FinProceso
