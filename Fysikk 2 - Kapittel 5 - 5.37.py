import numpy as np
import matplotlib.pyplot as plt

q1 = 1.0e-9
P1 = np.array([-0.05, 0])
q2 = -1.0e-9
d = np.linspace(0.01, 1)
P2 = np.array([0.05, 0])
k = 8.99e9

def f(x):
    return 1/x**2

x = np.linspace(0.01, 1)
def E_felt(r):
    r1 = r - P1
    r2 = r - P2
    e_r1 = r1/np.linalg.norm(r1)
    e_r2 = r2/np.linalg.norm(r2)
    E1 = k*q1/np.linalg.norm(r1)**2 * e_r1
    E2 = k*q2/np.linalg.norm(r2)**2 * e_r2
    E = E1 + E2
    return E
F = np.array([0, 0.2])
print(np.linalg.norm(E_felt(F)))

E_abs = []
for i in range(len(d)):
    P = np.array([0, d[i]])
    E = E_felt(P)
    E_abs = np.append(E_abs, np.linalg.norm(E))

plt.plot(x, f(x))
plt.plot(d, E_abs)
plt.grid()