from pylab import *

def f(x):
  return 3 - x*log(x/2 + 5)

x = linspace(-5, 7, 1000)
y = f(x)

plot(x, y, color = "b")
ylim(-20, 40)
axhline(y = 0, color = "b")
axvline(x = 0, color = "b")
xlabel("x")
ylabel("y")
grid()
show()

x1 = float(input("Skriv inn en x-verdi nær nullpunktet: "))

delta_x = 0.00001

def f_derivert(a):
  return (f(a + delta_x) - f(a)) / delta_x

def ny_x_verdi(x1):
  return x1 - (f(x1) / f_derivert(x1))

for i in range(10):
  x2 = ny_x_verdi(x1)
  print("Et bedre forslag er gitt ved x =", round(x2, 4))
  x1 = x2

print("Med x =", x1, " er f(x) =", f(x1))