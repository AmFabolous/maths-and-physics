from pylab import *

s = 0 
v = 0  
t = 0  

t_slutt = 10
dt = 0.01        
s_verdier = [s]  
t_verdier = [t]  
v_verdier = [v]  

def a(t): 
  return -0.40*t + 4.0          

while t < t_slutt:    
  v = v + a(t)*dt      
  s = s + v*dt        
  t = t + dt           
  s_verdier.append(s)  
  t_verdier.append(t)  
  v_verdier.append(v)  

plot(t_verdier, v_verdier)            
title("Fart som funksjon av tid")  
xlabel("$t$ (s)")                      
ylabel("$v$ (m/s)")                   
grid()                                
show()          

print("Bilen kommer",round(s,1),"meter på 10 sekunder")                       