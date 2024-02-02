import numpy as np

def reserva_rut_bd(base, rut):
    for user in base:
        ruts_reserva, asientos_reserva, valores_reserva, nombre, apellido = user

        for i in ruts_reserva:

            if i == rut:
                return True
            else:
                return False

def reserva_rut(base, rut):
    for user in base:
        if user == rut:
            return True
        else:
            return False

def listar_rut_ordenado(bd):
    listaRut = []
    for user in bd:
        ruts, asientos, valor, nombre, apellido = user

        for i in ruts:
            listaRut.append(i)

    listaRut.sort()

    return listaRut

def reserva_asiento(asientos, reserva):
    asientos[np.absolute(asientos) == reserva] = -1
    return asientos

def getDisponible(asientos, reserva):
    dispo = asientos[np.absolute(asientos == reserva)]
    return dispo

def asiento_reservado(asientos, asiento):
    x = getDisponible(asientos, asiento)
    if len(x) == 0:
        return False
    else:
        return True

def render_asientos_usados(reservados):
    usados_asientos = []
    for asientos in reservados:
        if asientos == -1:
            usados_asientos.append('X')
        else:
            usados_asientos.append(asientos)
    
    return np.array(usados_asientos)

def digito_verificador(rut):
    rut_invertido = str(rut)[::-1]
    valores = [2, 3, 4, 5, 6, 7]
    total = sum([int(rut_invertido[i]) * valores[i % 6] for i in range(len(rut_invertido))])
    resultado = 11-(total % 11)

    if resultado == 11:
        digito = 0
    elif resultado == 10:
        digito = "k"
    else:
        digito = resultado
    
    return digito

def valida_rut(rutUser):
    rut_sin_dv = rutUser.split("-")[0]
    rut_dv = rutUser.split("-")[1]
    isDV = str(digito_verificador(rut_sin_dv))

    if isDV == rut_dv.lower():
        return True
    else:
        return False