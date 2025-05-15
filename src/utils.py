class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        # Конструктор класса Product
        self.description = description
        self.name = name
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        # Магический метод для строкового представления объекта
        # Возвращает строку в формате: "Название, цена руб. Остаток: кол-во шт."
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # Магический метод
        # (цена * количество)
        if not isinstance(other, Product):
            # исключение
            return NotImplemented
        total = self.price * self.quantity + other.price * other.quantity
        return total

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
        # Метод добавления товара в категорию
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        return [str(product) for product in self.__products]

    def __str__(self):
        # Магический метод
        # Возвращает строку с названием и количеством товаров
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
