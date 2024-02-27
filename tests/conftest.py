import pytest
from models.category import Category
from models.customer import Customer
from models.employee import Employee
from models.menu_item import MenuItem
from models.order import Order

@pytest.fixture(scope='module')
def new_category():
    category_name = 'test_category'
    active = True
    parent_category_id = None

    category_attibute_values = {
       "category_name": category_name,
       "active": active,
       "parent_category_id": parent_category_id
    }

    category = Category(**category_attibute_values)

    return category

@pytest.fixture(scope='module')
def new_customer():
    first_name = 'Anya'
    last_name = 'Karph'
    email = 'anya_karph@gmail.com'

    customer_attibute_values = {
       "first_name": first_name,
       "last_name": last_name,
       "email": email
    }

    customer = Customer(**customer_attibute_values)

    return customer

@pytest.fixture(scope='module')
def new_employee():
    first_name = 'Alex'
    last_name = 'Simpson'
    email = 'alex_simpson@gmail.com'
    phone = '11-12-1345'
    position = 'chef'

    employee_attibute_values = {
       "first_name": first_name,
       "last_name": last_name,
       "email": email,
       "phone": phone,
       "position": position
    }

    employee = Employee(**employee_attibute_values)

    return employee

@pytest.fixture(scope='module')
def new_menu_item():
    menu_item_name = 'cappuccino'
    category_id = 3
    price = 3.4

    menu_item_attibute_values = {
       "menu_item_name": menu_item_name,
       "category_id": category_id,
       "price": price
    }

    menu_item = MenuItem(**menu_item_attibute_values)

    return menu_item

@pytest.fixture(scope='module')
def new_order():
    menu_item_id = 1
    customer_id = 1
    quantity = 1
    order_date = '2024-01-21'
    employee_id = 1

    order_attibute_values = {
       "menu_item_id": menu_item_id,
       "customer_id": customer_id,
       "quantity": quantity,
       "order_date": order_date,
       "employee_id": employee_id
    }

    order = Order(**order_attibute_values)

    return order