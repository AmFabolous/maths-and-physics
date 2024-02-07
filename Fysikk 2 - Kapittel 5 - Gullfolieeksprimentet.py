# Jeg tok med gravitasjon også, men den har virkelig ingenting å si for akselerasjonen

k = 8.99e9
m = 6.64e-27
M = 3.29e-25
q = 3.20e-19
Q = 1.26e-17
gamma = 6.67e-11

r = -1.0e-10
v = 1.5e7
t = 0
dt = 1.0e-22

def a(r):
    F_e = k*q*Q/r**2
    G = gamma*m*M/r**2
    return (G-F_e) / m

while v > 0:
    v = v + a(r)*dt
    r = r + v*dt
    t = t + dt

print(f'Alfapartikkelen snur når r = {r} m')