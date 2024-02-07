import math

def f(x):
    return math.exp(x)

a = 0
b = 1
n = 100000
dx = (b-a)/n
rsumV = 0
rsumH = 0

for i in range(n):
    rsumV += f(a + i*dx)*dx
    rsumH += f(a + (i+1)*dx)*dx

rsum = (rsumV + rsumH)/2

print(f'Integralet I er tilnærmet lik {round(rsum,2)}')


