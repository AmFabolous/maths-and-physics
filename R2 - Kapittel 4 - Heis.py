import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt('heis.txt')
tid = data[:,0]
aks = data[:,1]

def f(t, a, b):
    return a*b**t

[a, b] = curve_fit(f, tid, aks)[0]
print(f'a = {round(a, 2)}')
print(f'b = {round(b, 2)}')

print(f'En modell for aks kan være f(t) = {round(a, 2)}*{round(b, 2)}**t')

plt.xlabel('tid (s)')
plt.ylabel('akselerasjon (m/s^2)')
plt.plot(tid, aks)
plt.plot(tid, f(tid, a, b), 'k')
plt.grid()
plt.show()
