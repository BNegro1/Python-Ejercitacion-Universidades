Proceso descuento_articulo
	Definir nombre, clave Como Caracter;
	Definir precio como Entero;
	
	Escribir "ingrese el nombre del artículo: ";
	leer nombre;
	EScribir "ingrese precio del producto";
	leer precio;
	Repetir 
		Escribir "ingrese clave del producto(01/02)";
		leer clave;
	Hasta Que clave="01" o clave="02"
	si clave =="01" Entonces
		escribir "el precio con descuento es: ", precio*0.9;
	sino 
		escribir "el precio con descuento es: ", precio*0.8;
	FinSi
	
FinProceso
