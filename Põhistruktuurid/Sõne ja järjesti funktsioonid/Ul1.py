lists=[]
print(f'У вас есть список {lists}\nВыберити функцию добавления lists = []')


while True:
    try:
        print("1. Сумма числовых значений в списке\n2. Добавить элемент в список\n3. Удалить элемент из списка\n4. Очистить список\n5. Выход\n6. Отсортировать список\n7. Перевернуть список\n8. Найти индекс элемента\n9. Дублировать список\n10. Перемешать список\n11. Сделать срез списка")


        choice = int(input("Ваш выбор: "))
        if choice == 1:

            try:
                numeric_sum = sum(float(i) for i in lists)
                print(f'Сумма числовых значений в списке: {numeric_sum}')
            except ValueError:
                print("Ошибка: список содержит нечисловые элементы.")
        elif choice == 2:
            while True:
                try:
                    itemchose = int(input("Выберете что хотите добавить\n1.Строку/Слово\n2.Цифру/Число\n3.Что бы выйти с стадии добавления: "))
                    if itemchose == 1:
                        item=input("Ведите слово/строку которую хотите добавить: ")
                        lists.append(item)
                    elif itemchose == 2:
                        item=int(input("Ведите число/цифру которую хотите добавить"))
                        lists.append(item)
                    elif itemchose == 3: break
                except ValueError:
                    print("Error")
                print(f'Ваш список: {lists}')
        elif choice == 3:
            while True:
                try:
                    item = input("Введите элемент, который хотите удалить: ")
                    if item in lists:
                        lists.remove(item)
                        print(f'Ваш список: {lists}')
                        break
                    else:
                        print("Элемента нет в списке")
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
        elif choice == 4:
            lists.clear()
            print(f'Ваш список: {lists}')
        elif choice == 5:
            print("До свидания!")
            break
        elif choice == 6:
            try:
                lists.sort()
                print(f"Список отсортирован. Список: {lists}")
            except TypeError:
                print("Ошибка сортировки: элементы списка должны быть одного типа.")

        elif choice == 7:
            lists.reverse()
            print(f"Cписок перевёрнут. {lists}")
        elif choice == 8:
            element = input("Введите элемент для поиска индекса: ")
            if element in lists:
                print(f'Индекс элемента: {lists.index(element)}')
            else:
                print("Элемент не найден.")
        elif choice == 9:
            new_list = lists * 2
            print(f'Дублированный список: {new_list}')

        elif choice == 10:
            import random
            random.shuffle(lists)
            print(f"Список перемешан. {lists}")
        elif choice == 11:
            try:
                start = int(input("Введите начальный индекс: "))
                end = int(input("Введите конечный индекс: "))
                print(f'Срез списка: {lists[start:end]}')
            except ValueError:
                print("Ошибка ввода индексов.")


        else:
            print("Пожалуйста, выберите число от 1 до 11")

    except ValueError:
        print("Пожалуйста, введите число от 1 до 11")
