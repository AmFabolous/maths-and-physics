import numpy as np

m = 1.3
k = 0.24
g = 9.81
s = 6.0
v = 0

G = m*g
def a(v):
    L = k*v**2
    sum_F = L-G
    aks = sum_F/m
    return aks

t = 0
dt = 0.001

while s > 1.6:
    v = v + a(v)*dt
    s = s + v*dt
    t = t + dt

print(f'Farten til pakken når mannen griper den er {v:.2} m/s')