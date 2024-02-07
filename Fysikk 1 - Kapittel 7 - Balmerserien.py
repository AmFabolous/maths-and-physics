print("Energinivåene til spektrallinjene i balmerserien:")
print("")
B = 2.18*10**(-18)
c = 3*10**(8)
h = 6.63*10**(-34)

def E(n, m):
    return B*((1/m**2)-1/n**2)

for i in range(3, 30):
    dE = E(i, 2)
    f = dE/h
    l = h*c/dE
    dE = round(dE*10**18, 3)
    f = round(f*10**(-12))
    l = round(l*10**(9))
    if 400 < l < 700:
        a = "synlig lys"
    elif l < 400:
        a = "UV"
    else:
        a = "IR"
    print(f'Spektrallinje E{i}-E2: E = {dE} aJ, f = {f} THz, l = {l} nm ({a})')