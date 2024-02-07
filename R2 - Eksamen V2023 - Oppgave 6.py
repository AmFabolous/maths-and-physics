import numpy as np  # Importerer numpy-biblioteket for å få tilgang til ulike kommandoer

# Definerer øvre og nedre grenser
a = -1
b = 1

N = 10000   # Deler opp i 10000 rektangler
h = (b - a) / N     # Definerer bredden som øvre grense minus nedre grense delt på alle rektanglene

def g(x):    # Definerer g som roten av 1 - x^2
    return np.sqrt(1 - x**2)

S = 0   # Starter summen på 0

# Kjører en løkke 10000 ganger hvor den summerer alle delbuelengder til å finne total buelengde av graf
for i in range(N):      
    k = g(a + (i+1) * h) - g(a + i * h) # Den nye k-en blir g(x_(i+1)) - g(x_(i)); bruker x-en oppgitt i oppgaven
    S = S + np.sqrt(h**2 + k**2)    # Adderer på hver delbuelengde gitt ved roten av h^2 + k^2 til summen

print(round(S, 5))  # Printer buelengden av g fra -1 til 1 med avrunding på 5 desimaler



