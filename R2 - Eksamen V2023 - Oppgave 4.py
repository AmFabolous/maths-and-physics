# Definerer startpengene den første uka
a = 100
b = 100

# Definerer differansen i tilbud 1, og kvotienten i tilbud 2
d = 10
k = 1.05

# Lager for-løkker som printer ut det ukentlige beløpet i de 4 første ukene på hvert tilbud
print(f'Med tilbud 1:')
for i in range(4):
    print(f'Uke {i+1}: {a} kr')
    a = a + d        # Ukepengene øker med 10 kr for hver uke

print(f'')
print(f'Med tilbud 2:')
for i in range(4):
    print(f'Uke {i+1}: {round(b,2)} kr')    # Runder av til to desimaler
    b = b * k       # Ukepengene øker med 5% for hver uke 

