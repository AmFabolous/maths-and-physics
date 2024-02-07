import numpy as np
import matplotlib.pyplot as plt

m = 100
M = 5.972e24
gamma = 6.67e-11

r = np.array([4e7, 0])
v = np.array([0, 2.4e3])
t = 0

r_liste = [r]

def a(r):
    G_abs = gamma*m*M/(np.linalg.norm(r)**2)
    e_r = -r/np.linalg.norm(r)
    G = G_abs*e_r
    aks = G/m 
    return aks

dt = 10

while t < 1e5 and np.linalg.norm(r) > 6.371e6:
    v = v + a(r)*dt
    r = r + v*dt
    t = t + dt

    r_liste = np.concatenate([r_liste, [r]])

plt.axis("equal")
plt.title("Satelittbane")
plt.xlabel("x / m")
plt.ylabel("y / m")
plt.gca().add_artist(plt.Circle((0,0), 6.37e6))
plt.plot(r_liste[:, 0], r_liste[:, 1])
plt.show()