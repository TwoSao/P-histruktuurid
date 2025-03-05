while True:
    try:
        n=int(input("Sisetage arv:"))
        if n>0:
            break
        else:
            print("Sisestage ainult positiivne arv")
    except ValueError:
        print("See pole täisarv. Proovige uuesti.")
new = 0
while n > 0:
    k = n % 10
    new = new * 10 + k	
    n = n // 10
print(new)
    