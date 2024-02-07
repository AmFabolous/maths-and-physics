import numpy as np

m = 10000.0
c = 3.0e8
v = 0.1*c
F = 1000.0e3

dt = 1.00
tJ = 0
tR = 0
def g(v):
    return 1/np.sqrt(1 - (v/c)**2)

while tJ <= 24*60*60:
    v = c/ (np.sqrt(1+(m*c/(F*dt+g(v)*m*v))**2))
    tJ = tJ + dt
    tR = tR + dt/g(v)

    
print(f'Det har gått {tR/3600:.6} timer på romskipet etter 24 timer på jorda')