from pylab import *

a = 8.0
v = 0.0
t = 0.0
s = 0.0

dt = 0.01
t_slutt = 10.0
t_verdier = [t]
s_verdier = [s]
v_verdier = [v]
a_verdier = [a]

while t < t_slutt:
    a = 0.5*t + 8
    v = v + a*dt
    s = s + v*dt
    t = t + dt
    t_verdier.append(t)
    s_verdier.append(s)
    v_verdier.append(v)
    a_verdier.append(a)
   
    
plot(t_verdier, s_verdier)
title("Høyde som funksjon av tid")
xlabel("$t$(s)")
ylabel("$s$(m)")
grid()
show()

plot(t_verdier, v_verdier)
title("Fart som funksjon av tid")
xlabel("$t$(s)")
ylabel("$v$(m/s)")
grid()
show()

plot(v_verdier, a_verdier)
title("Akselerasjon som funksjon av tid")
xlabel("$t$(s)")
ylabel("$a$(m/s^2)")
grid()
show()

