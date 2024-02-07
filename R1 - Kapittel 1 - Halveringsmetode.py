from pylab import *

a=0
b=1

def f(x):
    return pi**x - 3

m = (a+b)/2
nøyaktighet = 0.0001

while abs(f(m)) >= nøyaktighet:
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m
        
    m = (a+b)/2
    
print("Løsningen er: ", round(m,4))