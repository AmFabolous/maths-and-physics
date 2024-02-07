# Oppgave 6.32
# b)

import numpy as np

a = 0
b = np.pi
n = 50
dx = (b - a) / n

def f(x):
    return np.sin(x)

rsumV = 0
rsumH = 0

for i in range(n):
    rsumV += f(a + i*dx) * dx
    rsumH += f(a + (i+1)*dx) * dx

rsum = (rsumV + rsumH) / 2

print(f'Integralet I er tilnærmet {rsum:.4f}')