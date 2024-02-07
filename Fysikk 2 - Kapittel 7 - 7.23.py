import numpy as np
import matplotlib.pyplot as plt

m = 0.05
B = 0.15
L = 0.2
R = 0.025
F_konstant = 1.0
v = 0
P = 0

def a(v):
    ems = v*L*B
    I = ems/R
    Fm = I*L*B
    sum_F = F_konstant - Fm
    return sum_F / m

def P1(v):
    ems = v*L*B
    I = ems/R
    effekt = ems*I
    return effekt

t = 0
s = 0
dt = 0.01
t_verdier = [t]
s_verdier = [s]
v_verdier = [v]
P_verdier = [P]

while t < 10:
    v = v + a(v) * dt
    s = s + v * dt
    P = P1(v)
    t = t + dt

    t_verdier = np.append(t_verdier, t)
    s_verdier = np.append(s_verdier, s)
    v_verdier = np.append(v_verdier, v)
    P_verdier = np.append(P_verdier, P)

plt.plot(t_verdier, s_verdier)
plt.plot(t_verdier, v_verdier)
plt.xlabel("tid / s")
plt.ylabel("strekning og fart")
plt.legend()
plt.grid()
plt.show()

plt.plot(v_verdier, P_verdier)
plt.xlabel("fart / (m/s)")
plt.ylabel("elektrisk effekt")
plt.grid()
plt.show()
