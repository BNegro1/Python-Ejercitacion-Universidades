#Cálculo de tiempo dilatado: Escribir un programa en Python que calcule el tiempo dilatado 
#para un objeto en movimiento a una velocidad cercana a la velocidad de la luz.
c = 3*(10**8)
def transformacionLorentzEinstein(vel, tiem):
    t_prima = (tiem/(1-(vel**2/c**2))**1/2)
    print("T': ", t_prima)
    return t_prima
v = int(input("Ingrese velocidad del objeto en movimiento: "))
t = int(input("Ingrese el tiempo medido en un sistema inercial (reposo): "))
transformacionLorentzEinstein(v, t)