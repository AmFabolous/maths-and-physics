# Programmet beregner bevegelsen til en 100-meter-løper
# som akselererer ut fra en startblokk. Bevegelsen
# presenteres som en v-s-graf.

from pylab import *

# Informasjon om bevegelsen
s = 0  # startposisjon, m
v = 0  # startfart, m/s
t = 0  # starttid, s

# Simuleringsteknisk
s_slutt = 100    # sluttposisjon, m
dt = 0.01        # lengde på tidssteg, s
s_verdier = [s]  # liste med verdier for posisjon
t_verdier = [t]  # liste med verdier for tid
v_verdier = [v]  # liste med verdier for fart

def a(v): # akselerasjonen er en funksjon av farten
  aks = -0.5*v + 6  # beregner akselerasjonen
  return aks        # returnerer akselerasjonen

# Løkka regner ut ny akselerasjon, fart og posisjon
# til løperen for hvert tidssteg
while s < s_slutt:     # etter 100 m er løpet over
  v = v + a(v)*dt      # beregner ny fart
  s = s + v*dt         # beregner ny posisjon
  t = t + dt           # øker tiden med dt
  s_verdier.append(s)  # legger s inn i posisjonslisten
  t_verdier.append(t)  # legger t inn i tidslisten
  v_verdier.append(v)  # legger v inn i fartslisten

# Tegning av graf
plot(t_verdier, s_verdier)              # lager grafen
title("Posisjon som funksjon av tid")  # tittel på grafen
xlabel("$t$ (s)")                       # x-akse-tittel
ylabel("$s$ (m)")                     # y-akse-tittel
grid()                                  # viser rutenett
show()                                  # viser grafen

print("Løperen bruker", round(t,1),"sekunder på å løpe 100 meter.")
