from random import *

konf=randint(1,100)
player=int(input("Mitu maiustust tahaksid laualt võtta?"))
#По умному
if player > konf:
    print(f"Laual pole magusat piisavalt, on ainult {konf}!")
    player=int(input("Sisestage kommide arv:"))
    print(f"Mõned kommid on alles {konf-player}")
else:
    print(f"Mõned kommid on alles {konf-player}")

# Если по простому то вот так
print(f"Lauale on jäänud natuke {konf-player}")

#Ul4
ocr=float(input("Sisenege ringi: "))
print(f"Puu läbimõõt on {ocr/3.14}")
