# Oppgave 4.37

import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 120
n = 10000
dt = (b - a) / n
v0 = 2

def vder(v):
    return 9.81 - 0.1*v

t = np.zeros(n)
v = np.zeros(n)

v[0] = v0

for i in range(n - 1):
    v[i + 1] = v[i] + vder(v[i]) * dt
    t[i + 1] = t[i] + dt

plt.plot(t, v)
plt.xlabel("Tid (s)")
plt.ylabel("Fart (m/s)")
plt.grid()
plt.show()

