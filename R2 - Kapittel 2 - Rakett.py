from pylab import *

data = loadtxt("rakett.txt")
tid = data[:,0]
fart = data[:,1]
n = len(tid)

dt = tid[1] - fart[0]
rsumV = 0
rsumH = 0

for i in range(n-1):
    rsumV += abs(fart[i])*dt
    rsumH += abs(fart[i+1])*dt
    
rsum = (rsumV + rsumH)/2
print(f'Raketten tilbakelegger ca. {round(rsum,3)} meter')

