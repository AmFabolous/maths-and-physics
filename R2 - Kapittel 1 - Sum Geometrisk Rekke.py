mulighet = int(input("(1) To tall i rekken // (2) et tall og en kvotient? (1/2)? "))
if mulighet == 1:
    tall_1 = float(input("Skriv inn det første tallet du har:"))
    tall_2 = float(input("Skriv inn det andre tallet du har:"))
    tall_1_rekke_nmr = int(input("Hvilket rekke nummer har tall 1?"))
    tall_2_rekke_nmr = int(input("Hvilket rekke nummer har tall 2?"))
    sum_antall = float(input("Skriv inn antall tall du har lyst å summere:"))
    k = float((tall_2 / tall_1)**(1/(tall_2_rekke_nmr - 1)))

    a_1 = float(tall_2 / (k**(tall_2_rekke_nmr - 1)))

    sum = a_1 * (k**(sum_antall)-1) / (k - 1)
    print(sum)

if mulighet == 2:
    tall_1 = float(input("Skriv tallet du har i rekken:"))
    tall_1_rekke_nmr = int(input("Hvilket rekke nummer har tall 1?"))
    kvotient = float(input("Skriv kvotienten du har fått oppgitt:"))
    k = kvotient
    sum_antall = int1(input("Skriv inn antall tall du har lyst å summere:"))
    a_1 = int(tall_1 / (k ** (tall_1_rekke_nmr - 1)))
    sum = a_1 * (k ** (sum_antall) - 1) / (k - 1)
    print(sum)

