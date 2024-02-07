import numpy as np

def f(x):
    return np.log(x+1)

y = 2

a = 0
b = np.exp(2) - 1
def flatestykke(x):
    return (f(x))**2 - y**2

n = 10000
dx = (b - a)/n
rsumV = 0
rsumH = 0

for i in range(n):
    rsumV += abs(flatestykke(a + i*dx)*dx)
    rsumH += abs(flatestykke(a + (i+1)*dx)*dx)

volum = np.pi*((rsumV + rsumH)/2)

print(f'Volumet av flatestykket dreid 360 grader om x-aksen er {round(volum, 1)}')

