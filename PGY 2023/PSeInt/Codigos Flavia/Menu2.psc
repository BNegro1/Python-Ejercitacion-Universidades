Algoritmo Menu2
	Definir n_opcion, edad, a_nacim, l_nombre, impares, num_ini, num_fin, i Como Entero;
	Definir nombre Como Caracter;
	n_opcion=1;
	
	
	Repetir
		
		Escribir "Elija una opci�n";
		Escribir "1. Mostrar impares";
		Escribir "2. Mostrar largo del nombre";
		Escribir "3. Calcular edad";
		Escribir "4. SALIR";
		Leer n_opcion;
		
		Si n_opcion==1 Entonces 
			Escribir "Ingrese n�mero de inicio";
			Leer num_ini;
			Escribir "ingrese n�mero de fin";
			Leer num_fin;
			Mientras num_ini <= num_fin Hacer
				Si num_ini mod 2 == 1 Entonces //si es par, sumar uno
					Escribir num_ini;
				FinSi				
				num_ini = num_ini + 1;				
			FinMientras		
			//otra opcion
			//para num = inicio hasta termino Hacer
				//si num mod 2 == 1 Entonces
					//escribir num
				//finsi
			//finpara
			
		SiNo
			Si n_opcion==2 Entonces
				Escribir "Ingrese nombre";
				Leer nombre;
				l_nombre = longitud(nombre);
				Escribir l_nombre;
			SiNo
				Si n_opcion==3 Entonces
					Repetir
						Escribir "Ingrese a�o de nacimiento";
						Leer a_nacim;						
						si a_nacim<1930 Entonces
							Escribir "a�o incorrecto, intentelo de nuevo";
							
						FinSi
					Hasta Que a_nacim > 1930 y a_nacim<2023
					edad=2023-a_nacim;
					Escribir "la edad es ", edad;
				sino 
					si n_opcion == 4 Entonces
						Escribir "Saliendo";
					SiNo
						Escribir "Ingrese una opci�n correcta";
					FinSi
					
					
				FinSi
			FinSi
		FinSi
		
	Hasta Que n_opcion==4
	
	
FinAlgoritmo

