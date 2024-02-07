import numpy as np

t = [0, 0.03, 0.06, 0.09, 0.12, 0.15]
eps = [0, -0.03, -0.13, -0.48, -1.28, 0]

dt = t[1] - t[0]
n = len(t)
rsumV = 0
rsumH = 0

for i in range(n-1):
    rsumV += eps[i]*dt
    rsumH += eps[i+1]*dt

rsum = (rsumV + rsumH)/2

print(f'Den største magnetsike fluksen var {-rsum} Vs')