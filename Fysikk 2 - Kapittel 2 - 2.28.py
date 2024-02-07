import numpy as np
import matplotlib.pyplot as plt

m_N = 62    # kg
m_M = 88    # kg 
k_N = 0.30  # kg/m
k_M = 0.60  # kg/m
g = 9.81    # m/s^2
v_0 = 25.828

# Beregner konstante krefter og definerer fartsvektorer og posisjonsvektor
G_N = np.array([0, -m_N*g])
G_M = np.array([0, -m_M*g])

v_N = np.array([v_0, 0])
v_M = np.array([v_0, 0])
s_N = np.array([0.0, 2.0])
s_M = np.array([0.0, 2.0])

def a_N(v_N):
    e_vN = v_N / np.linalg.norm(v_N)
    L_N = -k_N * np.linalg.norm(v_N)**2 * e_vN
    sumF_N = G_N + L_N
    aksN = sumF_N/m_N
    return aksN

def a_M(v_M):
    e_vM = v_M / np.linalg.norm(v_M)
    L_M = -k_M * np.linalg.norm(v_M)**2 * e_vM
    sumF_M = G_M + L_M
    aksM = sumF_M/m_M
    return aksM

t = 0
dt = 0.0001

def y(x):
    return 6.37e-5*x**3 - 0.0124*x**2

vN_liste = [v_N]
vM_liste = [v_M]
sN_liste = [s_N]
sM_liste = [s_M]


while s_N[1] > y(s_N[0]):
    v_N += a_N(v_N) * dt
    s_N += v_N * dt
    t += dt

    vN_liste = np.concatenate([vN_liste, [v_N]])
    sN_liste = np.concatenate([sN_liste, [s_N]])

while s_M[1] > y(s_M[0]):
    v_M += a_M(v_M) * dt
    s_M += v_M * dt
    t += dt

    vM_liste = np.concatenate([vM_liste, [v_M]])
    sM_liste = np.concatenate([sM_liste, [s_M]])

plt.plot(sN_liste[:,0], sN_liste[:, 1])
plt.plot(sM_liste[:,0], sM_liste[:, 1])
plt.plot(np.linspace(0, 130), y(np.linspace(0,130)))
plt.xlabel("x / m")
plt.ylabel("y / m")
plt.grid()
plt.show()

print(f'Nora hopper {s_N[0]} m og Martin hopper {s_M[0]} m')

import sympy as sp

x = sp.symbols('x')
funksjon = 6.37e-5*x**3 - 0.0124*x**2
buelengde_N = sp.integrate(sp.sqrt(1 + sp.diff(funksjon, x)**2),(x, 0, s_N[0])).evalf()
buelengde_M = sp.integrate(sp.sqrt(1 + sp.diff(funksjon, x)**2),(x, 0, s_M[0])).evalf()

print(f'Lengden av unnarennet er hhv. for Nora og Martin {buelengde_N} m og {buelengde_M} meter')


