import numpy as np

e = 1.6e-19
k = 8.99e9

qe = e
qp = e
me = 9.1094e-31
mp = 1.6726e-27

re = 0
rp = 1.0
r = rp - re

ve = 0
vp = 0

t = 0
dt = 0.000001


def F(r):
    F_e = k*qe*qp/r**2
    return F_e

while r >= 0:
    ve = ve + F(r)/me * dt
    vp = vp - F(r)/mp * dt
    re = re + ve * dt
    rp = rp + vp * dt
    t = t + dt
    r = rp - re
    print(r)

print(f'De to ladningene bruker {t} sekunder på å treffe hverandre')
    