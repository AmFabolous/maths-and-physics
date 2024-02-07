import numpy as np
import matplotlib.pyplot as plt

k = 8.99e9
mA = 0.1
mB = 0.5
qA = 5e-5
qB = -1e-4

vA = np.array([0, 10])
vB = np.array([0, -2])

rA = np.array([3, 0])
rB = np.array([0, 0])
R = np.linalg.norm(rB - rA)

def a(m, r):
    e_E = r/np.linalg.norm(r)
    E = -k*qA*qB/np.linalg.norm(r)**2 * e_E
    aks = E/m
    return aks

t = 0
dt = 0.0001
rA_liste = [rA]
rB_liste = [rB]

while rA[0] <= 3:
    r = rB - rA
    vA = vA + a(mA, r) * dt
    rA = rA + vA * dt
    vB = vB + a(mB, -r) * dt
    rB = rB + vB * dt
    t = t + dt

    rA_liste = np.concatenate([rA_liste, [rA]])
    rB_liste = np.concatenate([rB_liste, [rB]])

plt.plot(rA_liste[:, 0], rA_liste[:, 1])
plt.plot(rB_liste[:, 0], rB_liste[:, 1])
plt.grid()
plt.axis("equal")
plt.xlabel("x / m")
plt.ylabel("y / m")
plt.show()
print(t)
