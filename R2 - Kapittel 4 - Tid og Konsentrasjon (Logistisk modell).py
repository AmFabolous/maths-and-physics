import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import array, sin, linspace, e

tid = array([0, 1, 3, 5, 10])
konsentrasjon = array([0.025, 0.085, 0.28, 0.33, 0.33])

def K(t, C, a, b):
    return C/(1 + a*e**(-b*t))

[C, a, b] = curve_fit(K, tid, konsentrasjon)[0]
print(f'C = {round(C, 2)}')
print(f'a = {round(a, 2)}')
print(f'b = {round(b, 2)}')

plt.plot(tid, konsentrasjon, "o")
plt.xlabel("Tid (min)")
plt.ylabel("Konsentrasjon (mol/L)")
t = linspace(0, 15, 1000)
plt.ylim(0, 0.4)
plt.plot(t, K(t, C, a, b), "r")
plt.grid()
plt.show()
