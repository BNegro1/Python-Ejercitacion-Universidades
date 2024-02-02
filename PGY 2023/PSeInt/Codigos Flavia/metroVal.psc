Proceso metroVal
	definir hora, minutos, siguienteTren, hhmm Como Entero;
	Repetir
		Escribir "ingresar Hora [0-23]";
		leer hora;
	Hasta Que hora >=0 y hora <= 23
	Repetir 
		escribir "ingresar minutos [0-59]";
		leer minutos;
		
	Hasta Que minutos >=0 y minutos <= 59
	hhmm=(100*hora)+minutos; //cambiar formato hora a 100
	si hhmm >= 600 y hhmm <= 2230 Entonces
		escribir hora,":",minutos,"- metro funcionando";
		si hhmm<730 o hhmm > 900 Entonces
			escribir "horario normal -- frecuencia: cada 12 min";
			siguienteTren = 12- (minutos mod 12); //cuanto falta para el sgte tren
			si siguienteTren <> 12 Entonces
				escribir "el siguiente tren viene en: ", siguienteTren, " minutos. ";
			SiNo
				escribir "el tren ya está en el andén";
			FinSi
		sino 
			escribir "horario punta -- frecuencia cada 6 minutos";
			
			siguienteTren = 6- (minutos mod 6);
			si siguienteTren <> 6 Entonces
				escribir "el siguiente tren viene en: ", siguienteTren, " minutos.";
			SiNo
				escribir "el tren ya está en el andén";
			FinSi
		FinSi
	sino 
		escribir hora,":",minutos,"--el metro está cerrado a esa hora";
	FinSi
	
	
FinProceso
