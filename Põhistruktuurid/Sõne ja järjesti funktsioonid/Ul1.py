lists = []
print(f'Teil on nimekiri {lists}\nValige lisamisfunktsioon lists = []')

while True:
    try:
        print("1. Numbriliste väärtuste summa nimekirjas\n2. Lisa element nimekirja\n3. Eemalda element nimekirjast\n4. Tühjenda nimekiri\n5. Välju\n6. Sorteeri nimekiri\n7. Pöörake nimekiri\n8. Leia elemendi indeks\n9. Dubleeri nimekiri\n10. Sega nimekiri\n11. Tee lõige nimekirjast")

        choice = int(input("Teie valik: "))
        if choice == 1:
            try:
                numeric_sum = sum(float(i) for i in lists)
                print(f'Numbriliste väärtuste summa nimekirjas: {numeric_sum}')
            except ValueError:
                print("Tõrge: nimekiri sisaldab mittenumbrilisi elemente.")
        elif choice == 2:
            while True:
                try:
                    itemchose = int(input("Valige, mida soovite lisada\n1. Sõna/String\n2. Number\n3. Välju lisamisetapist: "))
                    if itemchose == 1:
                        item = input("Sisestage sõna/string, mida soovite lisada: ")
                        lists.append(item)
                    elif itemchose == 2:
                        item = int(input("Sisestage number, mida soovite lisada: "))
                        lists.append(item)
                    elif itemchose == 3:
                        break
                except ValueError:
                    print("Viga")
                print(f'Teie nimekiri: {lists}')
        elif choice == 3:
            while True:
                try:
                    item = input("Sisestage element, mida soovite eemaldada: ")
                    if item in lists:
                        lists.remove(item)
                        print(f'Teie nimekiri: {lists}')
                        break
                    else:
                        print("Elementi ei ole nimekirjas")
                except Exception as e:
                    print(f"Tekkis viga: {e}")
        elif choice == 4:
            lists.clear()
            print(f'Teie nimekiri: {lists}')
        elif choice == 5:
            print("Hüvasti!")
            break
        elif choice == 6:
            try:
                lists.sort()
                print(f"Nimekiri on sorditud. Nimekiri: {lists}")
            except TypeError:
                print("Sorteerimise viga: nimekirja elemendid peavad olema sama tüüpi.")
        elif choice == 7:
            lists.reverse()
            print(f"Nimekiri on pööratud. {lists}")
        elif choice == 8:
            element = input("Sisestage element indeksi leidmiseks: ")
            if element in lists:
                print(f'Elemendi indeks: {lists.index(element)}')
            else:
                print("Elementi ei leitud.")
        elif choice == 9:
            new_list = lists * 2
            print(f'Dubleeritud nimekiri: {new_list}')
        elif choice == 10:
            import random
            random.shuffle(lists)
            print(f"Nimekiri on segatud. {lists}")
        elif choice == 11:
            try:
                start = int(input("Sisestage algindeks: "))
                end = int(input("Sisestage lõppindeks: "))
                print(f'Nimekirja lõige: {lists[start:end]}')
            except ValueError:
                print("Indeksi sisestamise viga.")
        else:
            print("Palun valige number vahemikus 1 kuni 11")
    except ValueError:
        print("Palun sisestage number vahemikus 1 kuni 11")
