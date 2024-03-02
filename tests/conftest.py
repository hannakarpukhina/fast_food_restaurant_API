import pytest
from models.category import Category
from models.customer import Customer
from models.employee import Employee
from models.menu_item import MenuItem
from models.order import Order
from models.db_object import DBObject
from application import app
from tests.static.elements import (
    category_attributes,
    customer_attributes,
    employee_attributes,
    menu_item_attributes,
    order_attributes,
)


@pytest.fixture(scope="module")
def new_category():
    category = Category(**category_attributes)
    return category


@pytest.fixture(scope="module")
def new_customer():
    customer = Customer(**customer_attributes)
    return customer


@pytest.fixture(scope="module")
def new_employee():
    employee = Employee(**employee_attributes)
    return employee


@pytest.fixture(scope="module")
def new_menu_item():
    menu_item = MenuItem(**menu_item_attributes)
    return menu_item


@pytest.fixture(scope="module")
def new_order():
    order = Order(**order_attributes)
    return order


@pytest.fixture(scope="module")
def attribute_names():
    with app.app_context():
        attribute_names = Category.get_attribute_names()
        return attribute_names


@pytest.fixture(scope="module")
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client
