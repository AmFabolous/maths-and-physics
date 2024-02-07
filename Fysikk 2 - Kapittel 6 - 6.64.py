import numpy as np
import matplotlib.pyplot as plt

m = 1.5e-16
q = 0.10e-7
B = np.array([0, 0, -0.25])
ke = 8.99e9

v1 = np.array([0, 4.0e6, 0])
v2 = np.array([0, 4.0e6, 0])

r1 = np.array([-2.0e-3, 0, 0])
r2 = np.array([2.0e-3, 0, 0])

t = 0
dt = 1e-11

def a(v, ladning):
    M = q*np.cross(v, B) * ladning
    sum_F = M
    aks = sum_F / m
    return aks

r1x_liste = [r1[0]]
r1y_liste = [r1[1]]
r2x_liste = [r2[0]]
r2y_liste = [r2[1]]

while t < 1e-6:
    v1 = v1 + a(v1, 1) * dt
    v2 = v2 + a(v2, -1) * dt
    r1 = r1 + v1 * dt
    r2 = r2 + v2 * dt
    t = t + dt

    r1x_liste = np.append(r1x_liste, r1[0])
    r1y_liste = np.append(r1y_liste, r1[1])
    r2x_liste = np.append(r2x_liste, r2[0])
    r2y_liste = np.append(r2y_liste, r2[1])

plt.axis("equal")
plt.plot(r1x_liste, r1y_liste)
plt.plot(r2x_liste, r2y_liste)
plt.grid()
plt.show()