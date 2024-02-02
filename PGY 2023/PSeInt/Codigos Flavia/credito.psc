Proceso credito
	Definir estadoDicom Como Caracter;
	Definir ingresos Como Entero;
	Escribir "¿Se encuentra usted en DICOM? (Sí/No)";
	Leer estadoDicom;
	Escribir "¿Cuáles son sus ingresos mensuales?";
	Leer ingresos;
	
	Si estadoDicom == "No" y ingresos >= 500000 Entonces;
		Escribir "Usted puede optar a un crédito";
	Sino;
		Escribir  "Usted no puede optar a un crédito";
		
	FinSi
	
	
	
FinProceso
