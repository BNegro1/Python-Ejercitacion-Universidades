import tkinter as tk
import serial

# Inicializar conexión serial

# Funciones para abrir y cerrar la válvula
def abrir_valvula():
    puerto_serial.write(b'1')

def cerrar_valvula():
    puerto_serial.write(b'0')

# Crear ventana principal
ventana = tk.Tk()
ventana.title('Control de Válvula')

# Crear botones para abrir y cerrar la válvula
open_valve_btn = tk.Button(ventana, text='Abrir Válvula', command=abrir_valvula)
open_valve_btn.pack()

close_valve_btn = tk.Button(ventana, text='Cerrar Válvula', command=cerrar_valvula)
close_valve_btn.pack()

# Ejecutar la ventana principal
ventana.mainloop()

# Cerrar conexión serial
puerto_serial.close()
