import cowsay

a = 1
b = 1
sum = a + b
n = int(input("Antall n første fibbonaccitall som skal summeres: "))
if n == 1:
    print(f'Bruh, det er så vidt en sum. Men summen av de 1 første fibonaccitallene er 1')
elif n == 2:
    print(f'Summen av de to første fibonaccitallene er 2')

if n > 2:
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        sum += c
    cowsay.turtle(f'Summen av de {n} første fibonaccitallene er {sum}')
