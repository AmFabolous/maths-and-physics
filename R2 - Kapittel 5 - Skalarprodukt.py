import numpy as np

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
z1 = float(input('z1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
z2 = float(input('z2 = '))

u = np.array([x1, y1, z1])
v = np.array([x2, y2, z2])

if np.dot(u,v) == 0:
    print(f'u og v er ortogonale')
elif np.dot(u,v) > 0:
    print(f'Vinkelen mellom u og v er spiss')
else:
    print(f'Vinkelen mellom u og v er stump')

    