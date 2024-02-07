import matplotlib.pyplot as plt

# Initialverdier
v0 = 0.00   # Startfart (m/s)
s0 = 1.82   # Startposisjon (m)
dt = 0.001  # Tidsteg (s)
k  = 0.0044   # Dragkoeffisient (kg/m)
m  = 70e-3 / 45 # Massen til objektet (kg)
g  = 9.81   # Tyngdeakselrasjon (m/s^2)
t0 = 0.00  # 

a0 = (k*v0**2)/m - g
        
# tomme lister for å lagre tids- og posisjonsverdier for plotting
tidsverdier         = [t0]
akselerasjonsverdier = [a0]
fartsverdier        = [v0]
posisjonsverdier    = [s0]

# Iterer til objektet treffer bakken
while s0 > 0: 
    a = (k*v0**2)/m - g #finner a med N2L
    v = v0+a0*dt
    s = 0.5*a0*dt**2 + v0*dt+s0
    t = t0+dt
    
    # Lagre verdier for plotting
    tidsverdier.append(t)
    akselerasjonsverdier.append(a)
    fartsverdier.append(v)
    posisjonsverdier.append(s)
    
    #oppdaterer for neste runde i løkken
    t0=t
    a0=a
    v0=v
    s0=s

print(f'Tiden er {t:.3} sekunder')

