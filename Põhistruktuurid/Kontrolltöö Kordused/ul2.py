while True:
    try:
        l=int(input())
        if l > 0:
            break
        else:
            print("Sisestage positiivne arv")
        break
    except ValueError:
        print("See pole täisarv. Proovige uuesti.")
sum=0
for i in range(l+1):
    sum+=i
    print(sum)
print(sum)