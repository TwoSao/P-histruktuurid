from My import *

def main_menu():
    while True:
        print('1. Registreerimine\n2. Autoriseerimine\n3. Change password\n4. Password recovery\n5. Exit')
        try:
            choice = int(input('Valik: '))
            if choice == 1:
                while True:
                    a = input('Kas soovite jätkata? (1/0) ')
                    if a == '1':
                        writing()
                        break
                    elif a == '0':
                        break

            elif choice == 2:
                reading()
            elif choice == 3:
                change_password()
            elif choice == 4:
                password_recovery()
            elif choice == 5:
                break
            else:
                print('Vale valik')
        except ValueError:
            print('Vale valik')


if __name__ == '__main__':
    main_menu()