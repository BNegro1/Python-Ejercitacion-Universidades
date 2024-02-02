Proceso salario_semanal
	Definir horas, salario Como Entero;
	
	Escribir "Ingrese la cantidad de horas trabajadas";
	Leer horas;
	Si horas <= 40 Entonces;
		salario = 16 * 40;		
	SiNo
		salario=16*40 + (horas-40)*20;		
	FinSi
	Escribir "su salario semanal es de: $",salario;
FinProceso
