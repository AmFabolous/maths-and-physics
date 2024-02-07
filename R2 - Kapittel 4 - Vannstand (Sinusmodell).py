import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import array, sin, linspace

tid = array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])
vannstand = array([125, 199, 223, 176, 101, 73, 109, 181, 219, 188, 122, 85])

def h(t, A, phi, d):
    return A*sin(0.524*t + phi) + d

[A, phi, d] = curve_fit(h, tid, vannstand)[0]
print(f'A = {round(A, 2)}')
print(f'phi = {round(phi, 2)}')
print(f'd = {round(d, 2)}')

plt.plot(tid, vannstand, "o")
plt.xlabel("Tid (h)")
plt.ylabel("Vannstand (cm)")
t = linspace(0, 24, 1000)
plt.plot(t, h(t, A, phi, d), "r")
plt.grid()
plt.show()
