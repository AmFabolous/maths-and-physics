gamma = 6.67e-11
M = 5.974e24
R = 6371e3
r = 26000e3
v = 0
t = 0   # starter på tid = 0
dt = 0.1

while r > R:
    v = v + (gamma*M/r**2) * dt
    r = r - v*dt
    t = t + dt  # itererer gjennom tidsverdiene
print(v)
print(f'Tiden det tar før satelitten treffer jorda er {t} sekunder = {t/60} minutter')

