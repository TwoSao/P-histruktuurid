while True:
    try:
        n=abs(int(input("Sisestage arv: ")))
        break
    except ValueError:
        print("See pole täisarv. Proovige uuesti.")


summa = 0
tööd = 1
while n > 0:
    k = n % 10
    summa = summa + k
    n = n // 10
    tööd = tööd * k
print("Arvu summa on", summa)
print("Arvu korrutis on", tööd)