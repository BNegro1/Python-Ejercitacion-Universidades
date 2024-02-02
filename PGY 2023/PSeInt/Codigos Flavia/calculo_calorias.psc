Proceso calculo_calorias
	Definir horas_dor, horas_rep, calorias Como real;
	
	Escribir "ingrese la cantidad de horas en las que duerme";
	Leer horas_dor;
	Escribir "ingrese la cantidad de horas en las que reposa";
	leer horas_rep;
	
	calorias = horas_dor*60*1.08 + horas_rep*60*1.66;
	Escribir "Las calorías consumidas serán: ", calorias;
	
	
	
	
FinProceso
