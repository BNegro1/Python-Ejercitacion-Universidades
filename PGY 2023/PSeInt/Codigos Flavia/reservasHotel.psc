Proceso reservasHotel
	Definir precio, dias, cant_personas Como Entero;
	Definir rut, nombre, telefono, email Como Caracter;
	
	precio=35000;
	Escribir "ingrese su rut";
	leer rut;
	Escribir "ingrese su nombre";
	leer nombre;
	Escribir "ingrese su tel�fono";
	leer telefono;
	EScribir "ingrese su correo electr�nico";
	leer email;
	Escribir "�Por cuantos d�as desea hacer la reserva?";
	leer dias;
	Escribir "�Cu�ntas personas son?";
	leer cant_personas;
	
	Escribir "------------------------------------";
	Escribir "RESERVA HOTEL: ", mayusculas(nombre);
	Escribir "------------------------------------";
	Escribir rut,"     ",dias," D�AS     ",cant_personas," PERSONAS";
	Escribir "------------------------------------";
	Escribir "VALOR DIARIO POR PERSONA: $35000";
	Escribir "VALOR TOTAL: $",precio*cant_personas*dias;
FinProceso
