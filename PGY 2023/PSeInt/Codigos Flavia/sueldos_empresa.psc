Proceso sueldos_empresa
	Definir  num_empleados, i, a_servicio, cont1, cont2, cont3, sueldo_base como entero;
	Definir reajuste, sueldo, total_sueldos, total_sueldos_base, total_adicional Como Real;
	i=1;
	cont1=0;
	cont2=0;
	cont3=0;
	total_sueldos=0;
	total_sueldos_base=0;
	Escribir "ingrese el sueldo base: ";
	Leer sueldo_base;
	Escribir "Ingrese la cantidad de empleados: ";
	Leer num_empleados;
	Para i=1 Hasta num_empleados Hacer
		Repetir
			Escribir "Ingrese años de servicio del empleado n° ", i;
			Leer a_servicio;
			Si a_servicio >= 5 y a_servicio <=10 Entonces
				reajuste = 1.15;
				sueldo=sueldo_base*reajuste;
				Escribir "tiene un reajuste de 15% y su sueldo será de: ",sueldo;
				cont1=cont1+1;
			sino
				si a_servicio >= 11 y a_servicio <= 20 Entonces
					reajuste = 1.2;
					sueldo=sueldo_base*reajuste;
					Escribir "tiene un reajuste de 20% y su sueldo será de: ",sueldo;
					cont2=cont2+1;
				sino 
					si a_servicio > 20 Entonces
						reajuste = 1.25;
						sueldo=sueldo_base*reajuste;
						Escribir "tiene un reajuste de 25% y su sueldo será de: ",sueldo;
						cont3=cont3+1;
					
					FinSi
									
				FinSi
				
			FinSi
		Hasta Que a_servicio>=5
		total_sueldos=total_sueldos+sueldo;
		total_sueldos_base=total_sueldos_base+sueldo_base;
	
	FinPara
	total_adicional=total_sueldos-total_sueldos_base;
	
	Escribir "El dinero total por concepto de sueldos corresponde a: ",total_sueldos,".";
	Escribir "De ese monto, el dinero adicional por los reajustes corresponde a: ",total_adicional;
	Escribir cont1," empleados tendrán un reajuste del 15%, ",cont2," empleados del 20% y ",cont3," empleados del 25%";
	
	
	
FinProceso
