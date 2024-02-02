import matplotlib.pyplot as plt
import numpy as np

def runge_kutta(f, x0, p0, t0, h, n):
    x_list = [x0]
    p_list = [p0]
    t_list = [t0]
    
    for i in range(n):
        k1 = h * f(t_list[-1], x_list[-1], p_list[-1])
        l1 = h * p_list[-1]
        k2 = h * f(t_list[-1] + h/2, x_list[-1] + l1/2, p_list[-1] - k1/2)
        l2 = h * (p_list[-1] - k1/2)
        k3 = h * f(t_list[-1] + h/2, x_list[-1] + l2/2, p_list[-1] - k2/2)
        l3 = h * (p_list[-1] - k2/2)
        k4 = h * f(t_list[-1] + h, x_list[-1] + l3, p_list[-1] - k3)
        l4 = h * (p_list[-1] - k3)
        
        x_list.append(x_list[-1] + (l1 + 2*l2 + 2*l3 + l4)/6)
        p_list.append(p_list[-1] - (k1 + 2*k2 + 2*k3 + k4)/6)
        t_list.append(t_list[-1] + h)
        
    return np.array(t_list), np.array(x_list), np.array(p_list)

def f(t, x, p):
    return p

def g(t, x, p):
    return -x

frecuencia = float(input("Ingrese la frecuencia del oscilador: "))
amplitud = float(input("Ingrese la amplitud del oscilador: "))

x0 = amplitud
p0 = 0.0
t0 = 0.0
h = 0.01
n = 1000

t, x, p = runge_kutta(g, x0, p0, t0, h, n)

plt.plot(t, x, label='Posición')
plt.plot(t, p, label='Momento')
plt.xlabel('Tiempo')
plt.legend()
plt.show()
