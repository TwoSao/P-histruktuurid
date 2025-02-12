from random import *
#arv=randint(1, 2)
#if arv==5:
#    print("Arv on 5")
# Näidis 1
# print(arv)
#if arv==5:
#    print("Arv on 5")
#else:
#    print("Arv ei ole 5")
# Näidis 2
#if arv==5:
#    print("Arv on 5")
#elif arv==4:
#    print("Arv on 4")
#else:
#    print("Arv ei ole 4 ega 5")
# Näidis 3


# Ülesanne 1
try:
    nimi=input("Sisesta nimi: ")
    

vanus=int(input("Sisesta vanus: "))
if nimi.isupper() and nimi.islower():
    print("We go to the cinema")
else:
    print("We do not go to the cinema")
if vanus<=6:
    print("Cinema is free")
elif vanus<=14:
    print("Child ticket")
elif vanus<65:
    print("Adult ticket")
elif vanus>=65:
    print("Pensioner ticket")
elif vanus>100 or vanus<0:
    print("Invalid age")
# Ülesanne 2в
