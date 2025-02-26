import random

count = 0
tehed = ["+", "-", "*", "/"]
print("Valige tase \n1. tase \n2. tase \n3. tase")

while True:
    try:
        tase = int(input("Sisesta valik: "))
        if tase in [1, 2, 3]:
            break
        else:
            print("Palun sisesta ainult 1, 2 või 3.")
    except ValueError:
        print("Palun sisesta ainult täisarv.")

if tase == 1:
    num_examples = random.randint(1, 3)
    tehed1 = ["+", "-"]
elif tase == 2:
    num_examples = random.randint(4, 6)
else:
    num_examples = random.randint(7, 10)

for i in range(num_examples):
    if tase == 1:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        tehe = random.choice(tehed1)
    elif tase == 2:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        tehe = random.choice(tehed)
    else:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        tehe = random.choice(tehed)

    if tehe == "+":
        vastus = a + b
    elif tehe == "-":
        vastus = a - b
    elif tehe == "*":
        vastus = a * b
    else:
        vastus = a / b

    print(f"{a} {tehe} {b} = ?")
    while True:
        try:
            vastus1 = float(input("Sisesta vastus: "))
            break
        except ValueError:
            print("Palun sisesta ainult täisarv.")

    if vastus1 == vastus:
        print("Õige vastus!")
        count += 1
    else:
        print("Vale vastus!")

print(f"Teie skoor on {count}.")

protsent = (count / num_examples) * 100

if protsent < 60:
    hinne = 2
elif 60 <= protsent < 75:
    hinne = 3
elif 75 <= protsent < 90:
    hinne = 4
else:
    hinne = 5

print(f"Teie hinne on {hinne}.")
