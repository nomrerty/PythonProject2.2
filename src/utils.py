class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, price, quantity, description=" "):
        self.description = description
        self.name = name
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        required_atribute = ["name", "price", "quantity"]
        if not all(key in product_data for key in required_atribute):
            raise ValueError("Отсутствуют обязательные ключи: name, price, quantity")
        return cls(
            product_data["name"],
            product_data["price"],
            product_data["quantity"],
            product_data.get("description", "")
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class Smartphone(Product):
    def __init__(self, name, price, quantity, efficiency, model, memory, color, description=" "):
        super().__init__(name, price, quantity, description)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, price, quantity, country, germination_period, color, description=" "):
        super().__init__(name, price, quantity, description)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []
        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Можно добавлять только объекты класса Product или его наследников")

    @property
    def products(self):
        result = []
        for product in self.__products:
            result.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return result