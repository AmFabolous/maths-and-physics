def f(x):
    return 1/x
ln2 = 0.693147180559945

a = 1
b = 2
n = 1000000
dx = (b-a)/n
iterasjon = 0
rsumV = 0
rsumH = 0

for i in range(1, n):
    iterasjon += f(a + i*dx)
    
for i in range(n):
    rsumV += f(a + i*dx)*dx
    rsumH += f(a + (i+1)*dx)*dx

midtpunktsum = (rsumV + rsumH)/2
trapessum = (dx/2)*(f(a) + f(b) + 2*iterasjon)

print(f'Ulike metoder for en tilnærming av ln(2):')  
print(f'')  
print(f'Venstretilnærming: {rsumV}')
print(f'Høyretilnærming: {rsumH}')
print(f'Midtpunkttilnærming: {midtpunktsum}')
print(f'Trapessum: {trapessum}')

print(f'{ln2 - rsumV}')
print(f'{ln2 - rsumH}')
print(f'{ln2 - midtpunktsum}')
print(f'{ln2 - trapessum}')
