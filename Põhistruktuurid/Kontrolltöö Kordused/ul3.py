from random import *
arv=randint(0, 100)


katsed=10
for i in range(katsed):
    while True:
        try:
            n=int(input())
            if n>0:
                break
            else:
                print("Sisestage ainult positiivne arv")
            break
        except ValueError:
            print("See pole täisarv. Proovige uuesti.")
    if n>arv:
        print("Arv on väiksem")
    elif n<arv:
        print("Arv on suurem")
    else:
        print("Õige arv")
        break
if n!=arv:
    print("Õige arv oli", arv)

    