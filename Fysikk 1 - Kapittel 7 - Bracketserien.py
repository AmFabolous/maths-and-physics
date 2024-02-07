print("Energinivåene til de fire første spektrallinjene i bracketserien:")
B = 2.18*10**(-18)
c = 3E8
h = 6.63*10**(-34)

def E(n, m):
    return B*((1/m**2)-1/n**2)

for i in range(5, 20):
    dE = E(i, 4)
    f = dE/h
    λ = h*c/dE
    dE = round(dE*10**18, 3)
    f = round(f*10**(-12))
    λ = round(λ*10**(9))
    if 380 < λ < 740:
        a = "synlig lys"
    elif λ < 380:
        a = "UV"
    else:
        a = "IR"
    print(f'Spektrallinje E{i}-E4: E = {dE} aJ, f = {f} THz, λ = {λ} nm ({a})')