import numpy as np
import matplotlib.pyplot as plt

q = 1.0
m = 0.010
E = np.array([0, -0.0040, 0])
B = np.array([0, 0, -0.010])

F_e = q*E
def a(v):
    F_m = np.cross(q*v, B)
    sum_F = F_e + F_m
    aks = sum_F / m
    return aks

r = np.array([0, 0, 0])
v = np.array([0, 0, 0])
t = 0
dt = 0.001

x_verdier = [r[0]]
y_verdier = [r[1]]
v_verdier = [np.linalg.norm(v)]

while t < 14:
    v = v + a(v) * dt
    r = r+ v*dt
    t = t + dt
    x_verdier = np.append(x_verdier, r[0])
    y_verdier = np.append(y_verdier, r[1])
    v_verdier = np.append(v_verdier, np.linalg.norm(v))

plt.plot(x_verdier, y_verdier)
plt.title("Kryssede felt")
plt.xlabel("x / m")
plt.ylabel("v / m/s")
plt.grid()
plt.show()