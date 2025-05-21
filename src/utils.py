from abc import ABC, abstractmethod


class Product(ABC):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.description = description
        self.name = name
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    def new_product(cls, product_data):
        required_atribute = ["name", "description", "price", "quantity"]
        if not all(key in product_data for key in required_atribute):
            raise ValueError(
                "Отсутствуют обязательные ключи: name, description, price, quantity"
            )
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
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
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) != type(self):  #  использование type()
            raise TypeError("Нельзя складывать товары разных классов")
        return round(self.price * self.quantity + other.price * other.quantity, 2)


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) != type(self):  # Явное использование type()
            raise TypeError("Нельзя складывать товары разных классов")
        return round(self.price * self.quantity + other.price * other.quantity, 2)


class Category:
    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1
        if products:
            Category.product_count += len(products)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [str(product) for product in self.__products]

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
