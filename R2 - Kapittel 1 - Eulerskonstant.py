from pylab import *
a = 1
En = 0

for i in range(1,1000001): 
    a = 1/i
    En = En + a
    E = En - log(i)
    if i <= 100:
        print(E)
print("Eulerskonstant er tilnærmet lik",E)
    
    