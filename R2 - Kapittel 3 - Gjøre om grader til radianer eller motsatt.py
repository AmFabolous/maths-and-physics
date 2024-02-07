import math

x = int(input("Tast 1 om du vil gjøre om fra grader til radianer, eller 2 om du vil gjøre om fra radianer til grader: "))
if x == 1:
    y = float(input("Skriv inn antall grader: "))
    v = y*math.pi/180
    print(f'{x} deg tilsvarer {round(v,3)} rad')
    
elif x == 2:
    y = float(input("Skriv inn antall radianer: "))
    n = y*180/math.pi
    print(f'{x} rad tilsvarer {round(n,3)} deg')
    

