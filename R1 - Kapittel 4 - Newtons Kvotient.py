from pylab import *
def f(x):
    return 5*e**(-2*x)

def derivert(f, a, delta_x):
    return (f(a + delta_x) - f(a)) / delta_x

print("f'(1) =", derivert(f, 1, 1E-8))