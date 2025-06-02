class product:
    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = id

    def __eq__(self, other):
        return isinstance(other, product) and other.id == self.id


class shop:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.product_counts = {}
        self.carts = []

    def add_product(self, product: product, count: int = 1) -> bool:
        if not product.id:
            return False
        if product.name not in self.products:
            self.products[product.name] = product
            self.product_counts[product.id] = count
        else:
            self.product_counts[product.id] += count
        return True

    def get_product_count(self, product: product) -> int:
        if product.id not in self.product_counts:
            return -1
        return self.product_counts[product.id]

    def move_to_cart(self, product: product, count=1) -> bool:
        if product.id not in self.product_counts:
            return False
        if count > self.product_counts[product.id]:
            return False
        self.product_counts[product.id] -= count
        return True


class cart:
    def __init__(self, shop: shop):
        self.products = {}
        self.shop = shop

    def add_product(self, product: product, count=1) -> int:
        count_in_store = self.shop.get_product_count(product)
        if count_in_store <= 0:
            return count_in_store
        if count_in_store < count:
            count = count_in_store
        if not self.shop.move_to_cart(product, count):
            return 0
        self.products[product.id] = self.products.get(product.id, 0) + count
        return count

    def get_total_price(self):
        total_price = 0
        for pid, count in self.products.items():
            for p in self.shop.products.values():
                if p.id == pid:
                    total_price += p.price * count
                    break
        return total_price


if __name__ == "__main__":
    shop1 = shop("Illia")
    shop2 = shop("Illia2")

    p1 = product("Milk", 80, 1)
    p1a = product("Milk", 80, 1)
    p2 = product("Bread", 120, 2)

    shop1.add_product(p1, 10)
    shop1.add_product(p2, 10)
    print(shop1.products)

    c1 = cart(shop1)
    print(c1.add_product(p1, 4))
    print(shop1.product_counts)
    print(c1.products)
    print(c1.add_product(p1a, 4))
    print(c1.products)
    c1.add_product(p1, 3)
    print(c1.get_total_price())
    print(p1 == p1a)
