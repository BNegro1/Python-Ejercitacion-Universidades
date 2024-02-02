Algoritmo Menu
	Definir n_opcion, edad, a_nacim, l_nombre, impares, num_ini, num_fin, i Como Entero;
	Definir nombre Como Caracter;
	n_opcion=1
	Mientras n_opcion<4
		Repetir
			
			Escribir "Eliga una opción";
			Escribir "1. Mostrar impares";
			Escribir "2. Mostrar largo del nombre";
			Escribir "3. Calcular edad";
			Escribir "4. SALIR";
			Leer n_opcion
			
			Si n_opcion==1 Entonces 
				Escribir "Ingrese número de inicio";
				Leer num_ini;
				Escribir "ingrese número de fin";
				Leer num_fin;
				Mientras num_ini <= num_fin Hacer
					Si num_ini mod 2 == 0 Entonces //si es par, sumar uno
						num_ini = num_ini + 1
					FinSi
					Escribir num_ini
					num_ini = num_ini + 2				
				FinMientras					
				
			SiNo
				Si n_opcion==2 Entonces
					Escribir "Ingrese nombre";
					Leer nombre;
					l_nombre = longitud(nombre);
					Escribir l_nombre;
				SiNo
					Si n_opcion==3 Entonces
						Repetir
							Escribir "Ingrese año de nacimiento";
							Leer a_nacim;						
						Hasta Que a_nacim > 1930 y a_nacim<2023
						edad=2023-a_nacim
						Escribir "la edad es ", edad;
					sino 
						si n_opcion == 4 Entonces
							Escribir "Saliendo";
						SiNo
							Escribir "Ingrese una opción correcta";
						FinSi
						
						
					FinSi
				FinSi
			FinSi
			
		Hasta Que n_opcion > 0 y n_opcion < 5
	FinMientras
	
FinAlgoritmo
