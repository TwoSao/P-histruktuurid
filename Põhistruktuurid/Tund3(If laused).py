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

# nimi1 = input("Sisesta esimese inimese nimi: ")
# nimi2 = input("Sisesta teise inimese nimi: ")
# if nimi1 == 'Martin' or 'Illia' and nimi2 == 'Illia' or 'Martin':
#     print("Täna olete pinginaabrid")
# else:
#     print("Täna ei ole pinginaabrid")
#--------------------------------------------------
# if nimi1.isalpha() and nimi2.isalpha():
#     print("Täna olete pinginaabrid")
# else:
#     print("Täna ei ole pinginaabrid")

# Ülesanne 3

# try:
#     length = input("Sisestage toa pikkus meetrites: ")
#     width = input("Sisestage toa laius meetrites: ")
    
#     if length.replace('.', '', 1).isdigit() and width.replace('.', '', 1).isdigit():
#         length = float(length)
#         width = float(width)
#         area = length * width
#         print(f"Põranda pindala: {area} ruutmeetrit")
#     else:
#         print("Viga: Sisestage toa pikkuse ja laiuse jaoks õiged arvulised väärtused.")
        
#     renovation = input("Kas soovite remonti teha? (jah/ei): ").strip().lower()
    
#     if renovation in ("jah", "ei"):
#         if renovation == "jah":
#             price = input("Sisestage ruutmeetri hind: ").strip()
#             if price.replace('.', '', 1).isdigit():
#                 price = float(price)
#                 total_cost = area * price
#                 print(f"Põranda vahetamise maksumus: {total_cost} ühikut")
#             else:
#                 print("Viga: Sisestage ruutmeetri hinna jaoks õige arvuline väärtus.")
#         else:
#             print("Remonti pole vaja.")
#     else:
#         print("Viga: Sisestage 'jah' või 'ei'.")
# except Exception as e:
#     print(f"Tekkis viga: {e}")

# Ülesanne 4 - Soodushinna arvutamine

# try:
#     price = input("Sisestage algne hind: ")
#     if price.replace('.', '', 1).lstrip('-').isdigit():
#         price = float(price)
#         if price > 700:
#             discount_price = price * 0.7
#             print(f"Hind 30% allahindlusega: {discount_price} ühikut")
#         else:
#             print("Allahindlust ei rakendata, sest hind ei ületa 700.")
#     else:
#         print("Viga: Sisestage kehtiv arvuline väärtus.")
# except Exception as e:
#     print(f"Tekkis viga: {e}")

# Ülesanne 5 - Temperatuuri kontroll

# try:
#     temperature = input("Sisestage temperatuur: ")
#     if temperature.replace('.', '', 1).lstrip('-').isdigit():
#         temperature = float(temperature)
#         if temperature > 18:
#             print("Temperatuur on üle 18 kraadi (soovitatav toasoojus talvel).")
#         elif temperature == 18:
#             print("Temperatuur on täpselt 18 kraadi.")
#         else:
#             print("Temperatuur on 18 kraadi või alla selle.")
#     else:
#         print("Viga: Sisestage õige arvuline temperatuur.")
# except Exception as e:
#     print(f"Tekkis viga: {e}")

# Ülesanne 6

# a = int(input("Kui pikk sa oled?"))
# try:
#     if a < 150 or a > 220:
#         print("! ! !")
#     elif a >= 190:
#         print("Sa oled pikk!")
#     elif a >= 170:
#         print("Sa oled keskmine!")
#     else:
#         print("Sa oled lühike!")
# 
# except ValueError:
#     print("Viga! Sa oled kas liiga lühike või liiga pikk")

# Üllesane 7

# height = float(input("Enter your height in cm: "))
# gender = input("Enter your gender (male/female): ").lower()

# if gender == "male":
#     if height < 170:
#         print("You are short.")
#     elif 170 <= height <= 185:
#         print("You have an average height.")
#     else:
#         print("You are tall.")
# elif gender == "female":
#     if height < 160:
#         print("You are short.")
#     elif 160 <= height <= 175:
#         print("You have an average height.")
#     else:
#         print("You are tall.")
# else:
#     print("Invalid gender input.")

# Sisestame iga toote hinna ja koguse
# milk_price = float(input("Sisestage piima hind (EUR): "))
# bread_price = float(input("Sisestage leiva hind (EUR): "))
# bun_price = float(input("Sisestage kukli hind (EUR): "))

# Sisestame toodete koguse
# milk_quantity = int(input("Kui palju piima soovite osta? "))
# bread_quantity = int(input("Kui palju leiba soovite osta? "))
# bun_quantity = int(input("Kui palju kukleid soovite osta? "))

# Arvutame lõppsummat
# total_sum = (milk_price * milk_quantity) + (bread_price * bread_quantity) + (bun_price * bun_quantity)

# Trükime tšeki
# print("\nTšekk:")
# print(f"Piim ({milk_quantity} tk): {milk_price * milk_quantity:.2f} EUR")
# print(f"Leib ({bread_quantity} tk): {bread_price * bread_quantity:.2f} EUR")
# print(f"Kukkel ({bun_quantity} tk): {bun_price * bun_quantity:.2f} EUR")
# print(f"Kokku maksta: {total_sum:.2f} EUR")

# Ülesanne 9

# kylg1 = float(input("Sisesta ruudu esimene külg: "))
# kylg2 = float(input("Sisesta ruudu teine külg: "))

# if kylg1 == kylg2:
#     print("See on ruut.")
# else:
#     print("See ei ole ruut.")


# Ülesanne 10

# num1 = float(input("Sisesta esimene number: "))
# num2 = float(input("Sisesta teine number: "))

# operation = input("Sisesta tehe (+, -, *, /): ")
# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# elif operation == "/":
#     print(num1 / num2)
# else:
#     print("Vale tehe.")

# Ülesanne 11

# synniaasta = int(input("Sisesta oma sünniaasta: "))
# praegune_aasta = 2025  
# 
# if (praegune_aasta - synniaasta) % 10 == 0 or (praegune_aasta - synniaasta) % 25 == 0:
#     print("Palju õnne! See on juubel!")
# else:
#     print("See ei ole juubel.")


#--------------------------------------------------------
#12

# price = float(input("Введите цену товара: "))


# if price >= 10:
#     discount = 0.1 if price <= 10 else 0.2
#     final_price = price * (1 - discount)
# else:
#     final_price = price


# print(f"Окончательная цена товара: {final_price:.2f} евро")

#13

# gender = input("Enter the candidate's gender (male/female): ").lower()

# if gender == "female":
#     print("Candidate is not eligible: only males are allowed in the team.")
# else:
#     try:
#         age = int(input("Enter the candidate's age: "))
#         if 16 <= age <= 18:
#             print("Candidate is eligible for the team.")
#         else:
#             print("Candidate is not eligible: age must be between 16 and 18.")
#     except ValueError:
#         print("Error: age must be a number.")

#14

# people = int(input("Enter the number of people: "))
# bus_capacity = int(input("Enter the bus capacity: "))
# 
# buses_needed = people // bus_capacity
# if people % bus_capacity != 0:
#     buses_needed += 1
# 
# people_in_last_bus = people % bus_capacity
# if people_in_last_bus == 0:
#     people_in_last_bus = bus_capacity
# 
# print("Buses needed:", buses_needed)
# print("People in the last bus:", people_in_last_bus)