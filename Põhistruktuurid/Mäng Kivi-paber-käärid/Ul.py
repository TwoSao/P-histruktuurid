import random

score = 0
score2 = 0
lists = [1, 2, 3, 4]
while True:
    while True:
        try:
            chose = int(input("Valige, kellega soovite mängida\n1. Teise inimesega\n2. Robotiga\n3. Väljumine\n"))
            if chose in [1, 2, 3]:
                break
            else:
                print("Viga")
        except ValueError:
            print("Viga")

    if chose == 1:
        while True:
            try:
                player1 = int(input("Mängija 1. Valige objekt\n1. Kivi\n2. Käärid\n3. Paber\n4. Väljumine\n"))
                if player1 == 4:
                    break
                player2 = int(input("Mängija 2. Valige objekt\n1. Kivi\n2. Käärid\n3. Paber\n4. Väljumine\n"))
                if player2 == 4:
                    break
                if player1 in lists and player2 in lists:
                    pass
                else:
                    print("Viga")

            except ValueError:
                print("Viga")


            while player1 == player2:
                print(f"Viik! Teie skoor: {score}")
                try:
                    player1 = int(input("Mängija 1. Valige objekt\n1. Kivi\n2. Käärid\n3. Paber\n4. Väljumine\n"))
                    if player1 == 4:
                        break
                    player2 = int(input("Mängija 2. Valige objekt\n1. Kivi\n2. Käärid\n3. Paber\n4. Väljumine\n"))
                    if player2 == 4:
                        break
                    if player1 in lists and player2 in lists:
                        pass
                    else:
                        print("Viga")

                except ValueError:
                    print("Viga")


            if player1 == 4 or player2 == 4:
                break

            if (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (player1 == 3 and player2 == 1):
                score += 1
                print(f"Mängija 1 võitis! Mängija 1 skoor: {score}!\nMängija 1 valis: {player1}\nMängija 2 valis: {player2}")
            else:
                score2 += 1
                print(f"Mängija 2 võitis! Mängija 2 skoor: {score2}!\nMängija 1 valis: {player1}\nMängija 2 valis: {player2}")

    elif chose == 2:  # Игра с роботом
        while True:
            try:
                player1 = int(input("Mängija 1. Valige objekt\n1. Kivi\n2. Käärid\n3. Paber\n4. Väljumine\n"))
                if player1 == 4:
                    break
                if player1 in lists:
                    pass
                else:
                    print("Viga")

            except ValueError:
                print("Viga")


            player2 = random.choice([1, 2, 3])
            print(f"Robot valis: {player2}")

            if player1 == player2:
                print("Viik!")
                print(f"Mõlemad valisid: {player1}")
            elif (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (player1 == 3 and player2 == 1):
                score += 1
                print(f"Mängija 1 võitis! Mängija 1 skoor: {score}!\nMängija 1 valis: {player1}\nRobot valis: {player2}")
            else:
                score2 += 1
                print(f"Robot võitis! Roboti skoor: {score2}!\nMängija 1 valis: {player1}\nRobot valis: {player2}")

    elif chose == 3:
        break
