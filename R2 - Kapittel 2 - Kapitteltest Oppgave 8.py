import math

def f(x):
    return math.exp(x**2)

a = 1
b = 2
n = 100000
dx = (b - a)/n
volumV = 0
volumH = 0

for i in range(n):
    volumV += (f(a + i*dx))**2 * math.pi * dx
    volumH += (f(a + (i+1)*dx))**2 * math.pi * dx

volum = (volumV + volumH)/2

print(f'Volumet av omdreiningslegemet fra x = 1 til x = 2 blir {volum}')

