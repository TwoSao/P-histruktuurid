print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => "))))
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Pole mõtet nullist midagi ette võttaм")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Teeme kindlaks, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c = b = a
    paaris = 0
    paaritu = 0
    while b > 0:
        if b % 2 == 0:
            paaris =+ 1
        else:
            paaritu =+ 1
        b = b // 10
    
    print("Paarisarvud:",paaris)
    print("Paaritud numbrid:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake* sisestatud number")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine")
    print()
    if c % 2 == 0:
        print('{:>4}'.format(c), " - paarisarv. Jagage 2-ga.")
        c = c / 2
    else:
        print('{:>4}'.format(c), " - paaritu arv. Korrutage 3-ga, lisage 1 ja jagage 2.")
        c = (3*c + 1) / 2
    print()
    print("Hüpotees on õige")