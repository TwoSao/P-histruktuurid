while True:
    try:
        n=int(input())
        if n in [1,2,3,4,5,6,7,8,9]:
            break
        else:
            print("Sisestage ainult 1-9")
        
    
    except ValueError:
        print("See pole täisarv. Proovige uuesti.")

for i in range(n):
    print("   (\_/)", end=" ")
print()
for i in range(n):
    print("   (o o)", end=" ")
print()
for i in range(n):
    print("   / | \*", end=" ")
print()