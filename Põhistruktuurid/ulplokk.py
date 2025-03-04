from time import *
# V5 ul 3
for student in range(20):
    print(f"Soritab eksamit {student+1} õpilane")
    for exam in range(3):
        print(f"Soritab eksamit {exam+1} eksam")


# V4 ul 2
while True:
    try:
        p = int(input("Sisestage, mitu numbrit on loendis: "))
        break
    except ValueError:
        print("See pole täisarv. Proovige uuesti.")

negative_sum = 0
for num in range(p):
    while True:
        try:
            number1 = int(input("Sisestage täisarv: "))
            break
        except ValueError:
            print("See pole täisarv. Proovige uuesti.")
    if number1 < 0:
        negative_sum += number1
print(f"Negatiivsete arvude summa on: {negative_sum}")

# V3 ul 4
while True:
    try:
        kokku=int(input("Sisestage kotlettide arv: "))
        break
    except ValueError:
        print("See pole täisarv. Proovige uuesti.")
panni_math=int(input("Sisestage, mitu kotletti saab korraga praadida: "))
aeg=1
lahenemine = kokku//panni_math
jaak=kokku%panni_math
if jaak>0:
    lahenemine+=1
print(f"Kõik kotletid on praetud {lahenemine} pannitäiega")
for l in range(lahenemine):
    if jaak>0 and l==lahenemine-1:
        print(f"Panni peal on {jaak} kotletit")
    else:
        print(f"Panni peal on {panni_math} kotletit")
    print(f"{l+1}. lahenemine. Esimene pool")
    sleep(aeg)
    print("Ümberpööramine")
    print(f"{l+1}. lahenemine. Teine pool")
    sleep(aeg)
    print("Kotletid on valmis")
print("Kõik kotletid on praetud")
