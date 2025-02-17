print("Tere! Olen uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")
print("Kas leian Sinu keha indeksi? 0-ei, 1-jah")
try:
    soov = int(input("Sisesta 0 või 1: "))
    if soov == 1:
        try:
            pikkus = int(input("Sisesta oma pikkus sentimeetrites: "))
            try:
                mass = float(input("Sisesta oma kaal kilogrammides: "))
                indeks = mass / (0.01 * pikkus) ** 2
                print(f"{nimi}, Sinu keha indeks on: {round(indeks, 2)}")
                if indeks < 16:
                    print("Tervisele ohtlik alakaal")
                elif 16 <= indeks < 19:
                    print("Alakaal")
                elif 19 <= indeks < 25:
                    print("Normaalkaal")
                elif 25 <= indeks < 30:
                    print("Ülekaal")
                elif 30 <= indeks < 35:
                    print("Rasvumine")
                elif 35 <= indeks < 40:
                    print("Tugev rasvumine")
                else:
                    print("Tervisele ohtlik rasvumine")
            except ValueError:
                print("Vale sisend!")
        except ValueError:
            print("Vale sisend!")
    else:
        print("Kahju! See on väga kasulik info!")
except ValueError:
    print("Vale sisend!")