from numpy import *
import matplotlib.pyplot as plt

m = 35e-3
k = 2.0
L = 0.20
l = 0.15
g = 9.81
B = 0.50
R = 0.20

s = -0.30
v = 0
t = 0
dt = 0.01

def a(s, v):
    dx = s + l
    F = -k*dx
    G = -m*g
    Fm = -v * L**2 * B**2 / R
    sum_F = 2*F + G + Fm
    return sum_F/m

s_verdier = [s]
v_verdier = [v]
t_verdier = [t]

while t < 5:
    v = v + a(s, v) * dt
    s = s + v * dt
    t = t + dt

    s_verdier.append(s)
    v_verdier.append(v)
    t_verdier.append(t)

plt.plot(t_verdier, s_verdier)
plt.plot(t_verdier, v_verdier)
plt.grid()
plt.show()
