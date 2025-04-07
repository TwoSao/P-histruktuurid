def pood():
    # Initialize lists
    purchases = []
    prices = []
    bought = []

    # Fill the lists
    print("Введите количество продуктов, которые нужно купить:")
    count = int(input())
    for _ in range(count):
        product = input("Введите название продукта: ")
        price = float(input(f"Введите цену для {product}: "))
        purchases.append(product)
        prices.append(price)

    # Menu
    while True:
        print("\nМеню:")
        print("1. Удалить из списка купленный товар, добавить в список купил[] и составить чек")
        print("2. Отобразить в алфавитном порядке список покупок и их цены")
        print("3. Найти самый дорогой/дешевый товар")
        print("4. Найти цену запрашиваемого товара")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            product = input("Введите название купленного товара: ")
            if product in purchases:
                index = purchases.index(product)
                bought.append((product, prices[index]))
                del purchases[index]
                del prices[index]
                print(f"Товар {product} добавлен в список купленных.")
                print("Чек:")
                for item, price in bought:
                    print(f"{item}: {price}€")
                print(f"Итого: {sum(price for _, price in bought)}€")
            else:
                print("Товар не найден в списке покупок.")

        elif choice == "2":
            sorted_items = sorted(zip(purchases, prices), key=lambda x: x[0])
            print("Список покупок в алфавитном порядке:")
            for product, price in sorted_items:
                print(f"{product}: {price}€")

        elif choice == "3":
            if purchases:
                max_price = max(prices)
                min_price = min(prices)
                max_product = purchases[prices.index(max_price)]
                min_product = purchases[prices.index(min_price)]
                print(f"Самый дорогой товар: {max_product} ({max_price}€)")
                print(f"Самый дешевый товар: {min_product} ({min_price}€)")
            else:
                print("Список покупок пуст.")

        elif choice == "4":
            product = input("Введите название товара для поиска: ")
            if product in purchases:
                index = purchases.index(product)
                print(f"Цена товара {product}: {prices[index]}€")
            else:
                print("Товар не найден.")

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")