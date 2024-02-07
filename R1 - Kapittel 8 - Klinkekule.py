from pylab import *

# Lager arrays med tidene for hver av lengdene
tid1 = array([1.135, 1.3, 1.205, 1.145, 1.205])
tid2 = array([1.535, 1.48, 1.67, 1.665, 1.55])
tid3 = array([1.955, 1.935, 1.89, 1.99, 2.005])

# Definerer n som antall elementer (antall forsøk) i en av arrayene ovenfor
n = len(tid1)

# Finner ut av gjennomsnittstid, standardavvik og standardafeil for hver lengde
tid1_snitt = sum(tid1) / n
tid2_snitt = sum(tid2) / n
tid3_snitt = sum(tid3) / n
s1 = sqrt(sum((tid1 - tid1_snitt)**2) / (n - 1))
s2 = sqrt(sum((tid2 - tid2_snitt)**2) / (n - 1))
s3 = sqrt(sum((tid3 - tid3_snitt)**2) / (n - 1))
SE1 = s1 / sqrt(n)
SE2 = s2 / sqrt(n)
SE3 = s3 / sqrt(n)

# Lager arrays med lengdene, gjennomsnittstidene og standardfeilene
lengde = array([34, 67, 117])
y_snitt = array([tid1_snitt, tid2_snitt, tid3_snitt])
SE = array([SE1, SE2, SE3])

# Plotter tallene med lengde som førsteakse, gjennomsnittstid som andreakse med +- 2*standardfeil
plot(lengde, y_snitt, "b.")                             # "b." = blå
vlines(lengde, y_snitt - 2*SE, y_snitt + 2*SE, "r")     # "r" = rød

# Setter navn på første- og andreakse
xlabel("Lengde (cm)")
ylabel("Tid (s)")
show()
