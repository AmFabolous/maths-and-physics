# Oppgave 6.16

import sympy as sp

n = sp.symbols('n')
def f(n):
    return (n+2) / (2 ** (n-1))

sp.limit(f(n), n, sp.oo)

