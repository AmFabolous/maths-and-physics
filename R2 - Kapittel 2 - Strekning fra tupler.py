t = [0, 1, 2, 3, 4, 5, 6, 7, 8]
v = [0, 2, 6, 12, 19, 24, 28, 29, 30]

dt = t[1] - t[0]
n = len(t)
rsumV = 0
rsumH = 0

for i in range(n-1):
    rsumV += v[i]*dt
    rsumH += v[i+1]*dt

rsum = (rsumV + rsumH)/2
    
print(f'Strekning tilbakelagt regnet ved venstretilnærming er {rsumV} m')
print(f'Strekning tilbakelagt regnet ved høyretilnærming er {rsumH} m')
print(f'En bedre tilnærming blir gjennomsnittet, altså {rsum} m')

