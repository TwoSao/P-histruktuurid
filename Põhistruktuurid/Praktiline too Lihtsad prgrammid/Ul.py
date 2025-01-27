# from cgi import print_arguments
# from datetime import *
# from calendar import *
# from math import *
# from multiprocessing.util import sub_debug
# Ul1
# tana=date.today()
# print(f"Tere! Täna on {tana.strftime('%m/%d/%y')}")
# print(f"Tere! Täna on {tana.strftime('%b-%d-%Y')}")
# print(f"Tere! Täna on {tana.strftime('%b-%d-%Y')}")
# print(f"Tere! Täna on {tana.strftime('%b-%d-%Y')}")
# paevadekogus=monthrange(2026,1)[1]
# print(f"Jaanuaris on {paevadekogus}")
# paevad=date(tana.year, 12, 31)
# onjaanud=(paevad - tana).days
# print(f"Jaanuaris on jäänud {onjaanud} päeva")

# Ul2
# a=3+8/(4-2)*4
# print("Vatus: ", a) #See on tavaline matemaatika, sulgudes ütleme, mida kõigepealt teha
# a=3+(8/4)-2*4 # и так далее...
# a=(3+8)/4-2*4
# a=3+(8/4)-(2*4)

# Ul3
# try:
#     r=float(input("Radius on: "))
# except:
#     print("Sisesta ujikmaarvud!")
# ruudu_kulg=2*r
# ruudu_pindala=ruudu_kulg**2  
# ruudu_p=ruudu_kulg*4
# c=2*r*pi # периметр круга
# Scircle=pi*r**2
# print(f"Ruudu külg: {ruudu_kulg} ühikut, Ruudu pindala: {ruudu_pindala} ruutühikut, "
#       f"Ruudu ümbermõõt: {ruudu_p} ühikut, Ringi ümbermõõt: {c} ühikut, "
#       f"Ringi pindala: {Scircle} ruutühikut")

# Ul4
# d= 2.575 
# Maar=6378
# Maar*=100000
# Pmaa=2*pi*Maar
# Kogus=Pmaa/d
# print(f"Meil on vaja {int(Kogus):,d} mündi.")
# print(f"Meil on vaja {int(Kogus*2):,d} euro.")

# Ul5
# # Muutujad
# sõna1 = "kill-koll"
# sõna2 = "killadi-koll"
# print(f"{sõna1.capitalize()} {sõna1.capitalize()} {sõna2.capitalize()} {sõna1.capitalize()} {sõna1.capitalize()} {sõna2.capitalize()} {sõna1.capitalize()} {sõna1.capitalize()} {sõna1.capitalize()}")
# print(sõna1.capitalize())

# Ul6
# laul = """
# Rong see sõitis tsuhh tsuhh tsuhh,
# piilupart oli rongijuht.
# Rattad tegid rat tat taa,
# rat tat taa ja tat tat taa.
# Aga seal rongi peal,
# kas sa tead, kes olid seal?

# Rong see sõitis tuut tuut tuut,
# piilupart oli rongijuht.
# Rattad tegid kill koll koll,
# kill koll koll ja kill koll kill.
# """
# print(laul.upper())

# Ul7
# try:
#     a=float(input("Number üks: "))
#     b=float(input("Number kaks: "))
#     if a>0 and b>0:
#         print("Pindala ja nümbrtmõõdu rvutamine: ")
#         pindala=a*b
#         p=(a+b)*2
#         print(f"Ristküliku ümbermõõt: {p}, ristküliku pindala: {pindala}")
#     else:
#         print("Arvud peaval  suurem kui 0 olla!")

# except :
#     print("Sisesta ujikmaarvud!")

# #Ul8
# try:
    
#     kütuse=int(input("Kirjutage, kui palju kütust: "))
#     läbitud=int(input("Läbitud vahemaa km: "))
#     if kütuse>0 and läbitud>0:
#         summs=läbitud/kütuse
#         print(f"Kütusekulu 100 km kohta: {summs}")
#     else:
#         print("Arv peab olema suurem kui 0")

        
# except :
#      print("Väärtus peab olema numbriline")

# Ul9
# try:
#     M = float(input("Time: "))
#     kiirus = 29.9
#     if M>0:
#         distance = kiirus * (M / 60)
#         print(f"distance {distance:.2f} time {M} minutes.")
#     else:
#         print("Arv peab olema suurem kui 0")
# except :
#     print("Väärtus peab olema numbriline")
# M = float(input("Time: "))
# kiirus = 29.9 
# distance = kiirus * (M / 60)
# print(f"distance {distance:.2f} time {M} minutes.")

# ul10
# try:
#     minutid = int(input("Sisesta aeg minutites: "))
#     if minutid>0:
#        tunnid = minutid // 60
#        minutid_jarele = minutid % 60
#        print(f"{tunnid}:{minutid_jarele:02d}") # :02d форматирования целых чисел в двухзначное число
#     else:
#         print("Arv peab olema suurem kui 0")
# except:
#     print("Väärtus peab olema numbriline")