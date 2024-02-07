from pylab import *

m = 10
g = 9.81
k = 0.1
G = m*g

s = 0
v = 0
t = 0

def a(v):
    L = k*v**2
    sum_F = G - L
    return sum_F/m

s_slutt = 100
a_slutt = 0.1
t_slutt = 10
dt = 0.01
s_verdier = [s]
v_verdier = [v]
t_verdier = [t]

while s < s_slutt:
    v = v + a(v)*dt
    s = s + v*dt
    t = t + dt

    t_verdier.append(t)
    v_verdier.append(v)
    s_verdier.append(s)


plot(t_verdier, s_verdier)
title("Fart som funksjon av tid")
xlabel("$t$ / s")
ylabel("$v$ / (m/s)")
grid()
show()

print("Sluttfart:", v, "m/s")
print("Sluttid:", t, "s")