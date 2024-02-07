from pylab import *

v = 0.0
t = 0.0
s = 2.0
a = -9.81

dt = 0.01
t_slutt = 5

t_verdier = [t]
s_verdier = [s]

while t < t_slutt:
    if s > 0:
        v = v + a*dt
    else:
        v = -0.9*v
        
    s = s + v*dt
    t = t + dt
    t_verdier.append(t)
    s_verdier.append(s)
  
    
        

plot(t_verdier, s_verdier)
title("Høyde som funksjon av tid")
xlabel("$t$(s)")
ylabel("$s$(m)")
grid()
show()

print("Ballen bruker", round(t,1), "sekunder på å treffe bakken")
