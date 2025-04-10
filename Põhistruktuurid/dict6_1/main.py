from sonastik import *
def main():
    while True:
        choice = mainmenu()
        if choice == 1:
            translate_rus_to_est()
        elif choice == 2:
            translate_est_to_rus()
        elif choice == 3:
            add_word()
        elif choice == 4:
            change_word()
        elif choice == 5:
            testing()
        else:
            print("Invalid choice. Please try again.")
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != 'yes':
            break
if __name__=="__main__":
    main()