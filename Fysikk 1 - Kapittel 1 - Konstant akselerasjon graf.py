from pylab import *

s = 0.0
v = 0.0
a = 4.0
t = 0.0

t_slutt = 5.0
dt = 0.1
t_verdier = [t]
s_verdier = [s]
v_verdier = [v]

while t < t_slutt:
    v = v + a*dt
    s = s + v*dt
    t = t + dt
    t_verdier.append(t)
    v_verdier.append(v)
    
plot(t_verdier, v_verdier)
title("Fart som funksjon av tid")
xlabel("$t$ (s)")
ylabel("$v$ (m/s)")
grid()
show()