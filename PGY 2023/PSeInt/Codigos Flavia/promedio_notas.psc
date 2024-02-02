Proceso promedio_notas
	Definir nota,promedio, suma Como Real;
	Definir i Como Entero;
	i=1;
	suma = 0;
	Para i=1 Hasta 3 Hacer
		Repetir
			Escribir "Ingrese ", i,"a nota: ";
			Leer nota;
			
		Hasta Que nota <= 7.0 y nota > 1.0;
		
		suma=suma+nota;
	FinPara
	promedio = suma/3;
	Si promedio >= 3.95 Entonces
		Escribir "Ha aprobado la asignatura con nota ", promedio;
	Sino 
		Escribir "Ha reprobado la asignatura con nota ",promedio;
	FinSi
	
	
FinProceso
