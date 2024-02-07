import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import array, sin, linspace

diameter = array([0.19, 0.40, 0.70, 1.10, 1.40])
resistans = array([3.30, 0.75, 0.24, 0.099, 0.061])

def R(d, a, b):
    return a*d**b

[a, b] = curve_fit(R, diameter, resistans)[0]
print(f'a = {round(a, 2)}')
print(f'b = {round(b, 2)}')

plt.plot(diameter, resistans, "o")
plt.xlabel("Diameter (mm)")
plt.ylabel("Resistans (ohm)")
d = linspace(0, 2, 1000)
plt.ylim(-1, 20)
plt.plot(d, R(d, a, b), "r")
plt.grid()
plt.show()