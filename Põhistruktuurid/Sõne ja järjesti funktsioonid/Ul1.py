lists=[]
print(f'У вас есть список {lists}\nВыберити функцию добавления lists = []')

while True:
    print("\nЧто вы хотите сделать со списком?")
    print("1. Показать текущий список")
    print("2. Добавить элемент в список")
    print("3. Удалить элемент из списка")
    print("4. Очистить список")
    print("5. Выход")

    while True:
        try:
            choice = input("\nВведите номер функции, которую хотите выполнить: ")
            if choice>0: break
        except ValueError:
            print("Error")
    if choice == "1":
        print(f"\nТекущий список: {lists}")
    elif choice == "2":
        while True:
            try:
                element=input("add element: ")
                lists.append(element)
                break
            except ValueError:
                print("Error")


