# Oppgave 6.53
# b) & c)

import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 20
n = 10000
dt = (b - a) / n
v0 = 0
s0 = 0

def a(v):
    return 9.81 * (1 - (v**2) / (1.8**2))

t = np.zeros(n)
t1 = np.zeros(n)
v = np.zeros(n) 
s = np.zeros(n)

v[0] = v0
s[0] = s0
summen = 0

for i in range(n - 1):
    v[i+1] = v[i] + a(v[i]) * dt
    if summen < 12:
        summen = summen + v[i] * dt
        t2 = t[i]
    s[i+1] = s[i] + v[i] * dt
    t[i+1] = t[i] + dt

plt.plot(t, v)
plt.xlabel("Tid (s)")
plt.ylabel("Fart (m/s)")
plt.show()

plt.plot(t, s)
plt.xlabel("Tid (s)")
plt.ylabel("Posisjon (m/s)")
plt.show()

print(f'Det tar {t2} sekunder før muffinsformen har falt 12 meter.')
     