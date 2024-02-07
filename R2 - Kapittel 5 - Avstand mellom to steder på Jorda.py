import numpy as np

# Ber brukeren om bredde- og lengdegrader til to steder på Jorda
B1 = float(input("Breddegrad til første sted: "))
L1 = float(input("Lengdegrad til første sted: "))
B2 = float(input("Breddegrad til andre sted: "))
L2 = float(input("Lengdegrad til andre sted: "))

# Gjør om fra grader til radianer
B1_rad = np.radians(B1)
L1_rad = np.radians(L1)
B2_rad = np.radians(B2)
L2_rad = np.radians(L2)

# Radius av planet (i dette tilfellet jorda)
R = 6400
# Beregner de romlige koordinatene til stedene
x1 = R * np.cos(B1_rad) * np.cos(L1_rad)
y1 = R * np.cos(B1_rad) * np.sin(L1_rad)
z1 = R * np.sin(B1_rad)
x2 = R * np.cos(B2_rad) * np.cos(L2_rad)
y2 = R * np.cos(B2_rad) * np.sin(L2_rad)
z2 = R * np.sin(B2_rad)

# Lager posisjonsvektorer til begge stedene
sted_1 = np.array([x1, y1, z1])
sted_2 = np.array([x2, y2, z2])
# Finner lengdene til posisjonsvektorene
lengde_1 = np.sqrt(x1**2 + y1**2 + z1**2)
lengde_2 = np.sqrt(x2**2 + y2**2 + z2**2)

# Beregner avstanden ved bruk av skalarproduktet
vinkel = np.arccos((np.dot(sted_1, sted_2)) / (lengde_1 * lengde_2))
avstand = vinkel*6400
print(f'Avstanden mellom de to stedene er omtrent {avstand} km')

