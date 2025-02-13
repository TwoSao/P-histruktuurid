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
# nimi=input("Sisesta nimi: ")
# vanus=int(input("Sisesta vanus: "))
# if nimi.isupper() and nimi.islower():
#     print("We go to the cinema")
# else:
#     print("We do not go to the cinema")
# if vanus<=6:
#     print("Cinema is free")
# elif vanus<=14:
#     print("Child ticket")
# elif vanus<65:
#     print("Adult ticket")
# elif vanus>=65:
#     print("Pensioner ticket")
# elif vanus>100 or vanus<0:
#     print("Invalid age")

# Ülesanne 2
nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")
if nimi1 == 'Martin' or 'Illia' and nimi2 == 'Illia' or 'Martin':
    print("Täna olete pinginaabrid")
else:
    print("Täna ei ole pinginaabrid")
#--------------------------------------------------I
if nimi1.isalpha() and nimi2.isalpha():
    print("Täna olete pinginaabrid")
else:
    print("Täna ei ole pinginaabrid")