import numpy as np                     # importerer numpy-biblioteket

a = float(input("Skriv inn koordinat a: ")) # bruker taster inn alle koordinater
b = float(input("Skriv inn koordinat b: "))
c = float(input("Skriv inn koordinat c: "))
d = float(input("Skriv inn koordinat d: "))
e = float(input("Skriv inn koordinat e: "))
f = float(input("Skriv inn koordinat f: "))

A = (a, b)       # De bruker-tastede koordinatene blir satt inn i punktene A, B, C
B = (c, d)
C = (e, f)

AB = (c - a, d - b)     # Definerer alle vektorene som finnes i trekanten utifra punktene
AC = (e - a, f - b)

BA = (a - c, b - d)
BC = (e - c, f - d)

CA = (a - e, b - f)
CB = (c - e, d - f)

skalarproduktA = np.dot(AB, AC)     # Finner skalarproduktet mellom vektorene i hvert hjørne i trekanten
skalarproduktB = np.dot(BA, BC)
skalarproduktC = np.dot(CA, CB)

# Hvis noen av skalaproduktene blir 0, betyr det at vektorene i det ene hjørnet er ortogonal, som betyr rettvinklet trekant
if skalarproduktA == 0 or skalarproduktB == 0 or skalarproduktC == 0:   
    print(f'Punktene danner en rettvinklet trekant.')
else:
    print(f'Punktene danner ikke en rettvinklet trekant.')