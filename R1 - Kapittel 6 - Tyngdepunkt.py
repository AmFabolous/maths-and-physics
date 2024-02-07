import numpy as np

Ax = float(input(f'Skriv inn x-koordinaten til A: '))
Ay = float(input(f'Skriv inn y-koordinaten til A: '))
Bx = float(input(f'Skriv inn x-koordinaten til B: '))
By = float(input(f'Skriv inn y-koordinaten til B: '))
Cx = float(input(f'Skriv inn x-koordinaten til C: '))
Cy = float(input(f'Skriv inn y-koordinaten til C: '))

OA = np.array([Ax, Ay])
OB = np.array([Bx, By])
OC = np.array([Cx, Cy])

OT = 1/3 * (OA + OB + OC)
x_Tyngdepunkt = round(OT[0], 2)
y_Tyngdepunkt = round(OT[1], 2)

print(f'Koordinatene til tyngdepunktet er ({x_Tyngdepunkt},{y_Tyngdepunkt})')