Proceso credito
	Definir estadoDicom Como Caracter;
	Definir ingresos Como Entero;
	Escribir "�Se encuentra usted en DICOM? (S�/No)";
	Leer estadoDicom;
	Escribir "�Cu�les son sus ingresos mensuales?";
	Leer ingresos;
	
	Si estadoDicom == "No" y ingresos >= 500000 Entonces;
		Escribir "Usted puede optar a un cr�dito";
	Sino;
		Escribir  "Usted no puede optar a un cr�dito";
		
	FinSi
	
	
	
FinProceso
