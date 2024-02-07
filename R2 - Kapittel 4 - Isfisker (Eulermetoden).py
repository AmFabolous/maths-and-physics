# Oppgave 4.31

import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 600
n = 10000
dt = (b - a) / n
T0 = 37

def Tder(T):
    return -0.011*T

t = np.zeros(n)
T = np.zeros(n)

T[0] = T0

for i in range(n - 1):
    T[i + 1] = T[i] + Tder(T[i]) * dt
    t[i + 1] = t[i] + dt

plt.plot(t, T)
plt.xlabel("Tid (min)")
plt.ylabel("Kroppstemperatur (grader C)")
plt.grid()
plt.show()

