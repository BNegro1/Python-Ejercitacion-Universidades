Proceso calculadora_mejorada //11.	Idem anterior, pero permitiendo que el usuario pueda ir 
	//introduciendo de a un n�mero por vez y que en cada una de esas veces elija qu� operaci�n efectuar. 
	//Debe tener una memoria acumulativa y la posibilidad de poner a cero dicha memoria.
	//no se si realmente hice lo que ped�a el ejercicio
	definir suma, resta, producto, cociente, num1, num2, memoria Como Real;
	definir opcion1, opcion2 Como Caracter;
	Escribir "ingrese un n�mero";
	LEer num1;
	memoria = num1;
	Repetir
		
		Escribir "Elija una opci�n (S/R/P/C): ";
		Escribir "SUMA";
		Escribir "RESTA";
		Escribir "PRODUCTO";
		Escribir "COCIENTE";
		Leer opcion1;
		
		Si opcion1 == "S" Entonces
			Escribir "ingrese otro n�mero";
			LEer num2;
			Escribir memoria,"+",num2,"=", memoria+num2;
			memoria = memoria + num2;
		FinSi
		Si opcion1 == "R" Entonces
			Escribir "ingrese otro n�mero";
			LEer num2;
			Escribir memoria,"-",num2,"=",memoria-num2;
			memoria = memoria - num2;
		FinSi
		Si opcion1 == "P" Entonces
			Escribir "ingrese otro n�mero";
			LEer num2;
			Escribir memoria,"*",num2,"=", memoria*num2;
			memoria = memoria *num2;
		FinSi
		Si opcion1 == "C" Entonces
			Escribir "ingrese otro n�mero";
			LEer num2;
			Escribir memoria,"/",num2,"=", memoria/num2;
			memoria = memoria/num2;
		FinSi
		
		Repetir 
			Escribir "�Sigue calculando(S/N)?";
			leer opcion1;
			Si opcion1 <> "S" y opcion1 <> "N" Entonces
				escribir "Por favor ingrese una opci�n v�lida";
			FinSi
		hasta que opcion1 == "S" o opcion1 == "N"
		Si opcion1 == "S" entonces
			Escribir "�Desea resetear la memoria(S/N)?";
			leer opcion2;
			Si opcion2 == "S" Entonces
				Escribir "Borrando memoria...";
				ESCribir "ingrese un nuevo n�mero";
				leer memoria;
			FinSi
		finsi
		
		
	hasta que opcion1 = "N"
	
	Escribir "Se cierra el programa";
FinProceso
