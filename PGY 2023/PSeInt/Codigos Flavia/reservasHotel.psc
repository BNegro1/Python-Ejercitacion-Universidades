Proceso reservasHotel
	Definir precio, dias, cant_personas Como Entero;
	Definir rut, nombre, telefono, email Como Caracter;
	
	precio=35000;
	Escribir "ingrese su rut";
	leer rut;
	Escribir "ingrese su nombre";
	leer nombre;
	Escribir "ingrese su teléfono";
	leer telefono;
	EScribir "ingrese su correo electrónico";
	leer email;
	Escribir "¿Por cuantos días desea hacer la reserva?";
	leer dias;
	Escribir "¿Cuántas personas son?";
	leer cant_personas;
	
	Escribir "------------------------------------";
	Escribir "RESERVA HOTEL: ", mayusculas(nombre);
	Escribir "------------------------------------";
	Escribir rut,"     ",dias," DÍAS     ",cant_personas," PERSONAS";
	Escribir "------------------------------------";
	Escribir "VALOR DIARIO POR PERSONA: $35000";
	Escribir "VALOR TOTAL: $",precio*cant_personas*dias;
FinProceso
