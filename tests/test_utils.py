import pytest
from src.utils import Product, Category, Smartphone, LawnGrass


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield


def test_product_initialization():
    product = Smartphone("Test Product", "Test Description", 100.0, 10, "High", "Model", 128, "Black")
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    product1 = Smartphone("Product 1", "Desc 1", 50.0, 5, "High", "Model1", 64, "White")
    product2 = Smartphone("Product 2", "Desc 2", 75.0, 3, "High", "Model2", 128, "Black")
    products = [product1, product2]
    category = Category("Test Category", "Test Category Description", products)
    assert category.name == "Test Category"
    assert category.description == "Test Category Description"
    assert len(category.products) == 2
    assert category.products[0] == "Product 1, 50.0 руб. Остаток: 5 шт."
    assert category.products[1] == "Product 2, 75.0 руб. Остаток: 3 шт."


def test_category_count():
    product = Smartphone("Product", "Desc", 100.0, 1, "High", "Model", 128, "Black")
    category1 = Category("Cat1", "Desc1", [product])
    category2 = Category("Cat2", "Desc2", [product])
    assert Category.category_count == 2


def test_empty_category():
    category = Category("Empty Category", "No products here", [])
    assert category.name == "Empty Category"
    assert category.description == "No products here"
    assert category.products == []
    assert Category.product_count == 0
    assert Category.category_count == 1

def test_new_product_missing_attributes():
    product_data = {"name": "Test Product", "price": 200.0}
    with pytest.raises(
        ValueError,
        match="Отсутствуют обязательные ключи: name, description, price, quantity",
    ):
        Smartphone.new_product(product_data)


def test_add_product():
    category = Category("Test Category", "Test Description", [])
    product = Smartphone("Test Product", "Test Desc", 100.0, 5, "High", "Model", 128, "Black")
    category.add_product(product)
    assert len(category.products) == 1
    assert Category.product_count == 1
    assert category.products[0] == "Test Product, 100.0 руб. Остаток: 5 шт."


def test_add_invalid_product():
    category = Category("Test Category", "Test Description", [])
    with pytest.raises(
        TypeError, match="Можно добавлять только объекты класса Product"
    ):
        category.add_product("Not a Product")


def test_price_setter_valid():
    product = Smartphone("Test Product", "Test Desc", 100.0, 5, "High", "Model", 128, "Black")
    product.price = 200.0
    assert product.price == 200.0


def test_price_setter_invalid():
    product = Smartphone("Test Product", "Test Desc", 100.0, 5, "High", "Model", 128, "Black")
    original_price = product.price
    product.price = -100
    assert product.price == original_price
    product.price = 0
    assert product.price == original_price


def test_products_property_format():
    product = Smartphone("Test Product", "Test Desc", 150.0, 20, "High", "Model", 128, "Black")
    category = Category("Test Category", "Test Description", [product])
    expected_format = "Test Product, 150.0 руб. Остаток: 20 шт."
    assert category.products == [expected_format]


def test_product_str():
    product = Smartphone("Apple", "Green apple", 100.0, 10, "High", "Model", 128, "Black")
    assert str(product) == "Apple, 100.0 руб. Остаток: 10 шт."


def test_category_str():
    product1 = Smartphone("Apple", "Green apple", 100.0, 5, "High", "Model1", 64, "White")
    product2 = Smartphone("Banana", "Yellow banana", 200.0, 10, "High", "Model2", 128, "Yellow")
    category = Category("Food", "Food category", [product1, product2])
    assert str(category) == "Food, количество продуктов: 15 шт."


def test_product_add():
    product1 = Smartphone("Apple", "Green apple", 100.0, 10, "High", "Model1", 64, "White")
    product2 = Smartphone("Banana", "Yellow banana", 200.0, 2, "High", "Model2", 128, "Yellow")
    assert product1 + product2 == 1400.0


def test_product_add_invalid():
    product = Smartphone("Apple", "Green apple", 100.0, 10, "High", "Model", 128, "Black")
    with pytest.raises(TypeError):
        product + 5


def test_smartphone_creation():
    smartphone = Smartphone(
        name="iPhone 13",
        description="Смартфон Apple",
        price=999.99,
        quantity=5,
        efficiency="Высокая",
        model="iPhone 13",
        memory=128,
        color="Черный"
    )
    assert smartphone.name == "iPhone 13"
    assert smartphone.description == "Смартфон Apple"
    assert smartphone.price == 999.99
    assert smartphone.quantity == 5
    assert smartphone.efficiency == "Высокая"
    assert smartphone.model == "iPhone 13"
    assert smartphone.memory == 128
    assert smartphone.color == "Черный"
    assert str(smartphone) == "iPhone 13, 999.99 руб. Остаток: 5 шт."


def test_lawn_grass_creation():
    grass = LawnGrass(
        name="Газонная трава",
        description="Трава для газона",
        price=299.99,
        quantity=10,
        country="Россия",
        germination_period=14,
        color="Зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.description == "Трава для газона"
    assert grass.price == 299.99
    assert grass.quantity == 10
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "Зеленый"
    assert str(grass) == "Газонная трава, 299.99 руб. Остаток: 10 шт."


def test_product_price_setter():
    smartphone = Smartphone(
        name="iPhone 13",
        description="Смартфон Apple",
        price=999.99,
        quantity=5,
        efficiency="Высокая",
        model="iPhone 13",
        memory=128,
        color="Черный"
    )
    smartphone.price = 899.99
    assert smartphone.price == 899.99
    smartphone.price = -100
    assert smartphone.price == 899.99


def test_smartphone_addition():
    smartphone1 = Smartphone(
        name="iPhone 13",
        description="Смартфон Apple",
        price=999.99,
        quantity=2,
        efficiency="Высокая",
        model="iPhone 13",
        memory=128,
        color="Черный"
    )
    smartphone2 = Smartphone(
        name="iPhone 14",
        description="Смартфон Apple",
        price=1099.99,
        quantity=3,
        efficiency="Высокая",
        model="iPhone 14",
        memory=256,
        color="Белый"
    )
    total = smartphone1 + smartphone2
    expected = round((999.99 * 2) + (1099.99 * 3), 2)
    assert total == expected


def test_lawn_grass_addition():
    grass1 = LawnGrass(
        name="Газонная трава 1",
        description="Трава для газона",
        price=299.99,
        quantity=5,
        country="Россия",
        germination_period=14,
        color="Зеленый"
    )
    grass2 = LawnGrass(
        name="Газонная трава 2",
        description="Трава для газона",
        price=399.99,
        quantity=3,
        country="США",
        germination_period=10,
        color="Темно-зеленый"
    )
    total = grass1 + grass2
    expected = round((299.99 * 5) + (399.99 * 3), 2)
    assert total == expected


def test_invalid_product_addition():
    smartphone = Smartphone(
        name="iPhone 13",
        description="Смартфон Apple",
        price=999.99,
        quantity=2,
        efficiency="Высокая",
        model="iPhone 13",
        memory=128,
        color="Черный"
    )
    grass = LawnGrass(
        name="Газонная трава",
        description="Трава для газона",
        price=299.99,
        quantity=10,
        country="Россия",
        germination_period=14,
        color="Зеленый"
    )
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = smartphone + grass


def test_category_creation():
    category = Category("Электроника", "Электронные товары")
    assert category.name == "Электроника"
    assert category.description == "Электронные товары"
    assert len(category.products) == 0
    assert str(category) == "Электроника, количество продуктов: 0 шт."


def test_category_add_product():
    category = Category("Электроника", "Электронные товары")
    smartphone = Smartphone(
        name="iPhone 13",
        description="Смартфон Apple",
        price=999.99,
        quantity=2,
        efficiency="Высокая",
        model="iPhone 13",
        memory=128,
        color="Черный"
    )
    category.add_product(smartphone)
    assert len(category.products) == 1
    assert category.products[0] == "iPhone 13, 999.99 руб. Остаток: 2 шт."
    assert str(category) == "Электроника, количество продуктов: 2 шт."


def test_category_add_invalid_product():
    category = Category("Электроника", "Электронные товары")
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product("Не продукт")


def test_category_product_count():
    Category.product_count = 0
    category = Category("Электроника", "Электронные товары")
    smartphone1 = Smartphone(
        name="iPhone 13",
        description="Смартфон Apple",
        price=999.99,
        quantity=2,
        efficiency="Высокая",
        model="iPhone 13",
        memory=128,
        color="Черный"
    )
    smartphone2 = Smartphone(
        name="iPhone 14",
        description="Смартфон Apple",
        price=1099.99,
        quantity=3,
        efficiency="Высокая",
        model="iPhone 14",
        memory=256,
        color="Белый"
    )
    category.add_product(smartphone1)
    assert Category.product_count == 1
    category.add_product(smartphone2)
    assert Category.product_count == 2


def test_infoprintmixin_prints_on_init(capsys):
    product = Product("Продукт1", "Описание продукта", 1200, 10)
    captured = capsys.readouterr()
    assert "Product('Продукт1', 'Описание продукта', 1200, 10)".split("(")[0] in captured.out