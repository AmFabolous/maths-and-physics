import numpy as np
import matplotlib.pyplot as plt

q1 = 2.0e-9
P1 = np.array([0, 0])
q2 = -2.0e-9
P2 = np.array([0.01, 0])
k = 8.99e-9

def E_felt(r):
    r1 = r - P1
    r2 = r - P2
    e_r1 = r1/np.linalg.norm(r1)
    e_r2 = r2/np.linalg.norm(r2)
    E1 = k*q1/np.linalg.norm(r1)**2 * e_r1
    E2 = k*q2/np.linalg.norm(r2)**2 * e_r2
    E = E1 + E2
    return E

punkt = np.array([0, 0.01])
E = E_felt(punkt)

print(f'Det elektriske feltet i punktet {punkt} er {E}.')
print(f'Det har en absoluttverdi på {np.linalg.norm(E):.3} V/m')
print(f'Vinkelen mellom feltretningen og x-aksen er {np.degrees(np.arctan(E[1]/E[0])):.3}')
