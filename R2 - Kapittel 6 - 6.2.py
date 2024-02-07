# Oppgave 6.2
# a)
a = 1
for i in range(1, 51):
    print(f"{i}: {a}")
    a = a + i

# b)
a = 1
for i in range(1, 51):
    a_neste = a + i
    print(f'{i}: {a_neste - a}')
    a = a_neste

# c)
a = 1
summen = 0
for i in range(1, 51):
    summen = summen + a
    a = a + i
print(f'Summen av de 50 første leddene er {summen}')


    