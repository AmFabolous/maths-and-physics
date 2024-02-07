def f(x):
    return 0.06*x**2 + 4*x - 7
    
def snittfart(f, x1, x2):
    return (f(x2) - f(x1)) / (x2-x1)

x1 = float(input("Tast inn nedre grense: "))
x2 = float(input("Tast inn øvre grense: "))

snitt = round(snittfart(f,x1,x2),2)

print("Gjennomsnittlig vekstfart i intervallet [",x1,",", x2, "] er ", snitt)
