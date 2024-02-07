from pylab import *
delta_x = 1E-8
def f(x):
 return -3*x**3 + 4*x**2 - 5*x + 10

def derivert(a):
 return (f(a + delta_x) - f(a)) / delta_x

def derivert_eksakt(x):
 return -9*x**2 + 8*x - 5

x_verdier = linspace(-5, 5, 100)
dy_verdier = derivert(x_verdier)
dy_eksakte_verdier = derivert_eksakt(x_verdier)
plot(x_verdier, dy_verdier)
plot(x_verdier, dy_eksakte_verdier)
show()  