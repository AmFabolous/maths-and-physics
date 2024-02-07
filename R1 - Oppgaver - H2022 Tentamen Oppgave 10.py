a = 0.0001
b = 4
noyaktighet = 0.01

def f(x):
    return (x**2 - 4*x + 3)/(x - 2)

m = (a + b)/2
    
while abs(f(m)) >= noyaktighet:
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m
    m = (a + b)/2

a = -0.0001

n = (a + b)/2
    
while abs(f(n)) >= noyaktighet:
    if f(a) * f(n) < 0:
        b = n
    else:
        a = n
    n = (a + b)/2

print(f'Løsningene på likningen er tilnærmet lik {round(m, 4)} og {round(n, 4)}')
