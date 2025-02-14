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
#     print("Lähme kinno")
# else:
#     print("Me ei lähe kinno")
# if vanus<=6:
#     print("Kino on tasuta")
# elif vanus<=14:
#     print("Lastepilet")
# elif vanus<65:
#     print("Täispilet")
# elif vanus>=65:
#     print("Pensionäri pilet")
# elif vanus>100 or vanus<0:
#     print("Kehtetu vanus")

# Ülesanne 2

# nimi1 = input("Sisesta esimese inimese nimi: ")
# nimi2 = input("Sisesta teise inimese nimi: ")
# if nimi1 == 'Martin' või 'Illia' ja nimi2 == 'Illia' või 'Martin':
#     print("Täna olete pinginaabrid")
# else:
#     print("Täna ei ole pinginaabrid")
#--------------------------------------------------
# if nimi1.isalpha() ja nimi2.isalpha():
#     print("Täna olete pinginaabrid")
# else:
#     print("Täna ei ole pinginaabrid")

# Ülesanne 3

# try:
#     pikkus = input("Sisestage toa pikkus meetrites: ")
#     laius = input("Sisestage toa laius meetrites: ")
    
#     if pikkus.replace('.', '', 1).isdigit() ja laius.replace('.', '', 1).isdigit():
#         pikkus = float(pikkus)
#         laius = float(laius)
#         pindala = pikkus * laius
#         print(f"Põranda pindala: {pindala} ruutmeetrit")
#     else:
#         print("Viga: Sisestage toa pikkuse ja laiuse jaoks õiged arvulised väärtused.")
        
#     remont = input("Kas soovite remonti teha? (jah/ei): ").strip().lower()
    
#     if remont in ("jah", "ei"):
#         if remont == "jah":
#             hind = input("Sisestage ruutmeetri hind: ").strip()
#             if hind.replace('.', '', 1).isdigit():
#                 hind = float(hind)
#                 kogumaksumus = pindala * hind
#                 print(f"Põranda vahetamise maksumus: {kogumaksumus} ühikut")
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
#     hind = input("Sisestage algne hind: ")
#     if hind.replace('.', '', 1).lstrip('-').isdigit():
#         hind = float(hind)
#         if hind > 700:
#             soodushind = hind * 0.7
#             print(f"Hind 30% allahindlusega: {soodushind} ühikut")
#         else:
#             print("Allahindlust ei rakendata, sest hind ei ületa 700.")
#     else:
#         print("Viga: Sisestage kehtiv arvuline väärtus.")
# except Exception as e:
#     print(f"Tekkis viga: {e}")

# Ülesanne 5 - Temperatuuri kontroll

# try:
#     temperatuur = input("Sisestage temperatuur: ")
#     if temperatuur.replace('.', '', 1).lstrip('-').isdigit():
#         temperatuur = float(temperatuur)
#         if temperatuur > 18:
#             print("Temperatuur on üle 18 kraadi (soovitatav toasoojus talvel).")
#         elif temperatuur == 18:
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
#     if a < 150 või a > 220:
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

# pikkus = float(input("Sisesta oma pikkus cm: "))
# sugu = input("Sisesta oma sugu (mees/naine): ").lower()

# if sugu == "mees":
#     if pikkus < 170:
#         print("Sa oled lühike.")
#     elif 170 <= pikkus <= 185:
#         print("Sul on keskmine pikkus.")
#     else:
#         print("Sa oled pikk.")
# elif sugu == "naine":
#     if pikkus < 160:
#         print("Sa oled lühike.")
#     elif 160 <= pikkus <= 175:
#         print("Sul on keskmine pikkus.")
#     else:
#         print("Sa oled pikk.")
# else:
#     print("Kehtetu soo sisestus.")

# Sisestame iga toote hinna ja koguse
# piima_hind = float(input("Sisestage piima hind (EUR): "))
# leiva_hind = float(input("Sisestage leiva hind (EUR): "))
# kukli_hind = float(input("Sisestage kukli hind (EUR): "))

# Sisestame toodete koguse
# piima_kogus = int(input("Kui palju piima soovite osta? "))
# leiva_kogus = int(input("Kui palju leiba soovite osta? "))
# kukli_kogus = int(input("Kui palju kukleid soovite osta? "))

# Arvutame lõppsummat
# kogusumma = (piima_hind * piima_kogus) + (leiva_hind * leiva_kogus) + (kukli_hind * kukli_kogus)

# Trükime tšeki
# print("\nTšekk:")
# print(f"Piim ({piima_kogus} tk): {piima_hind * piima_kogus:.2f} EUR")
# print(f"Leib ({leiva_kogus} tk): {leiva_hind * leiva_kogus:.2f} EUR")
# print(f"Kukkel ({kukli_kogus} tk): {kukli_hind * kukli_kogus:.2f} EUR")
# print(f"Kokku maksta: {kogusumma:.2f} EUR")

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

# tehe = input("Sisesta tehe (+, -, *, /): ")
# if tehe == "+":
#     print(num1 + num2)
# elif tehe == "-":
#     print(num1 - num2)
# elif tehe == "*":
#     print(num1 * num2)
# elif tehe == "/":
#     print(num1 / num2)
# else:
#     print("Vale tehe.")

# Ülesanne 11

# synniaasta = int(input("Sisesta oma sünniaasta: "))
# praegune_aasta = 2025  
# 
# if (praegune_aasta - synniaasta) % 10 == 0 või (praegune_aasta - synniaasta) % 25 == 0:
#     print("Palju õnne! See on juubel!")
# else:
#     print("See ei ole juubel.")


#--------------------------------------------------------
#12

# hind = float(input("Sisestage toote hind: "))


# if hind >= 10:
#     allahindlus = 0.1 kui hind <= 10 else 0.2
#     lõpphind = hind * (1 - allahindlus)
# else:
#     lõpphind = hind


# print(f"Toote lõpphind: {lõpphind:.2f} eurot")

#13

# sugu = input("Sisestage kandidaadi sugu (mees/naine): ").lower()

# if sugu == "naine":
#     print("Kandidaat ei ole sobilik: ainult mehed on lubatud meeskonda.")
# else:
#     try:
#         vanus = int(input("Sisestage kandidaadi vanus: "))
#         if 16 <= vanus <= 18:
#             print("Kandidaat on sobilik meeskonda.")
#         else:
#             print("Kandidaat ei ole sobilik: vanus peab olema 16 ja 18 vahel.")
#     except ValueError:
#         print("Viga: vanus peab olema number.")

#14

# inimesed = int(input("Sisestage inimeste arv: "))
# bussi_maht = int(input("Sisestage bussi mahutavus: "))
# 
# vaja_busse = inimesed // bussi_maht
# kui inimesed % bussi_maht != 0:
#     vaja_busse += 1
# 
# inimesed_viimases_bussis = inimesed % bussi_maht
# kui inimesed_viimases_bussis == 0:
#     inimesed_viimases_bussis = bussi_maht
# 
# print("Vajalikud bussid:", vaja_busse)
# print("Inimesed viimases bussis:", inimesed_viimases_bussis)
