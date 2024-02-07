k = 8.99e9
m = 6.64e-27
q = 3.20e-19
Q = 1.26e-17

r = -1.0e-10
v = 1.5e7
t = 0
dt = 1.0e-22

def a(r):
    F_e = k*q*Q/r**2
    return -F_e / m

while r < -5.0e-12:
    v = v + a(r)*dt
    r = r + v*dt
    t = t + dt

print(f'Farten er {v} m/s når avstanden er 5e-12 m')