# Oppgave 4.33

import numpy as np
import matplotlib.pyplot as plt 

a = 0
b = 240
n = 10000
dt = (b - a) / n
N0 = 50
k = 0.06
B = 500

def Nder(N):
    return k*N * (1 - N/B)

t = np.zeros(n)
N = np.zeros(n)

N[0] = N0

for i in range(n - 1):
    N[i + 1] = N[i] + Nder(N[i]) * dt
    t[i + 1] = t[i] + dt

plt.plot(t, N)
plt.xlabel("Tid (måneder)")
plt.ylabel("Harepopulasjon")
plt.grid()
plt.show()

