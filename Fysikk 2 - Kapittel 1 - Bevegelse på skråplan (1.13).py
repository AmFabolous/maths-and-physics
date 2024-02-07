import numpy as np
import matplotlib.pyplot as plt

# Konstanter
m = 0.400
theta = np.radians(30)
my = 0.35
g = 9.81

# Konstante krefter
Gx = m*g*np.sin(theta)
Gy = m*g*np.cos(theta)
N = Gy

# Variable krefter, utregning av kraftsum og akselerasjon
def a(v):
    R = -np.sign(v)*my*N
    sum_F = -Gx + R
    akselerasjon = sum_F/m
    return akselerasjon

# Startverdier
s = 0
v = 3.20
t = 0

# Liste for lagring av data
s_verdier = [s]
v_verdier = [v]
t_verdier = [t]

# Simulering av bevegelse
dt = 0.001

while s >= 0:
    v = v + a(v)*dt
    s = s + v*dt
    t = t + dt

    # Lagring av verdier
    v_verdier.append(v)
    s_verdier.append(s)
    t_verdier.append(t)

# Tegning av graf
plt.plot(t_verdier, v_verdier)
plt.xlabel("$t$ / s")
plt.ylabel("$v$ / (m/s)")
plt.title("Fartsgraf langs skråplan")
plt.grid()
plt.show()



