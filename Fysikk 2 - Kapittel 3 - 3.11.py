m_j = 5.972e24 
m_m = 7.35e22
r_j = 6371000.0
r_m = 1738000.0
gamma = 6.67e-11
r0 = 380000000.0

def a(r, m):
    G = gamma*m_j*m_m/r**2
    sum_F = G
    aks = sum_F/m
    return aks

R_j = 0.0
R_m = r0
v_j = 0.0
v_m = 0.0
R = R_m - R_j

t = 0
dt = 0.01

while R > (r_j + r_m):
    v_j += a(R, m_j) * dt
    v_m = v_m - a(R, m_m) * dt
    R_j += v_j * dt
    R_m += v_m * dt
    R = R_m - R_j
    t = t + dt
print(f'Tiden det tar før jorda og månen kolliderer er {t/3600:.5} timer')