from pylab import *

delta_x = 1E-8

def f(x):
    return -3*x**3)+4*x**2-5*x+10

def derivert(a):
    return (f(a+ delta_x) - f(a)) / delta_x

x_verdier = linspace(-5, 5, 100)
y_verdier = f(x_verdier)
dy_verdier = derivert(x_verdier)

plot(x_verdier, y_verdier)
plot(x_verdier, dy_verdier)
show()
