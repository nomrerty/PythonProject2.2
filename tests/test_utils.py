import pytest
from src.utils import Product, Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield


def test_product_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    product1 = Product("Product 1", "Desc 1", 50.0, 5)
    product2 = Product("Product 2", "Desc 2", 75.0, 3)
    products = [product1, product2]
    category = Category("Test Category", "Test Category Description", products)
    assert category.name == "Test Category"
    assert category.description == "Test Category Description"
    assert len(category.products) == 2
    assert category.products[0] == "Product 1, 50.0 руб. Остаток: 5 шт."
    assert category.products[1] == "Product 2, 75.0 руб. Остаток: 3 шт."


def test_category_count():
    product = Product("Product", "Desc", 100.0, 1)
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


def test_new_product():
    product_data = {
        "name": "Test Product",
        "description": "Test Desc",
        "price": 200.0,
        "quantity": 15,
    }
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.description == "Test Desc"
    assert product.price == 200.0
    assert product.quantity == 15


def test_new_product_missing_attributes():
    product_data = {"name": "Test Product", "price": 200.0}
    with pytest.raises(
        ValueError,
        match="Отсутствуют обязательные ключи: name, description, price, quantity",
    ):
        Product.new_product(product_data)


def test_add_product():
    category = Category("Test Category", "Test Description", [])
    product = Product("Test Product", "Test Desc", 100.0, 5)
    category.add_product(product)
    assert len(category.products) == 1
    assert Category.product_count == 1
    assert category.products[0] == "Test Product, 100.0 руб. Остаток: 5 шт."


def test_add_invalid_product():
    category = Category("Test Category", "Test Description", [])
    with pytest.raises(
        ValueError, match="Можно добавлять только объекты класса Product"
    ):
        category.add_product("Not a Product")


def test_price_setter_valid():
    product = Product("Test Product", "Test Desc", 100.0, 5)
    product.price = 200.0
    assert product.price == 200.0


def test_price_setter_invalid():
    product = Product("Test Product", "Test Desc", 100.0, 5)
    original_price = product.price
    product.price = -100
    assert product.price == original_price
    product.price = 0
    assert product.price == original_price


def test_products_property_format():
    product = Product("Test Product", "Test Desc", 150.0, 20)
    category = Category("Test Category", "Test Description", [product])
    expected_format = "Test Product, 150.0 руб. Остаток: 20 шт."
    assert category.products == [expected_format]


def test_product_str():
    product = Product("Apple", "Green apple", 100.0, 10)
    assert str(product) == "Apple, 100.0 руб. Остаток: 10 шт."


def test_category_str():
    product1 = Product("Apple", "Green apple", 100.0, 5)
    product2 = Product("Banana", "Yellow banana", 200.0, 10)
    category = Category("Food", "Food category", [product1, product2])
    assert str(category) == "Food, количество продуктов: 15 шт."


def test_product_add():
    product1 = Product("Apple", "Green apple", 100.0, 10)
    product2 = Product("Banana", "Yellow banana", 200.0, 2)
    assert product1 + product2 == 1400.0


def test_product_add_invalid():
    product = Product("Apple", "Green apple", 100.0, 10)
    with pytest.raises(TypeError):
        product + 5
