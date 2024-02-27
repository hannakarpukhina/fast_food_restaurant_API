def test_new_category_with_fixture(new_category):
    """
    GIVEN a Category model
    WHEN a new Category is created
    THEN check the category_name, active, and parent_category_id fields are defined correctly
    """
    assert new_category.category_name == 'test_category'
    assert new_category.active == True
    assert new_category.parent_category_id == None


def test_new_customer_with_fixture(new_customer):
    """
    GIVEN a Customer model
    WHEN a new Customer is created
    THEN check the first_name, last_name, and email fields are defined correctly
    """
    assert new_customer.first_name == 'Anya'
    assert new_customer.last_name == 'Karph'
    assert new_customer.email == 'anya_karph@gmail.com'

def test_new_employee_with_fixture(new_employee):
    """
    GIVEN a Employee model
    WHEN a new Employee is created
    THEN check the first_name, last_name, email, phone and position fields are defined correctly
    """
    assert new_employee.first_name == 'Alex'
    assert new_employee.last_name == 'Simpson'
    assert new_employee.email == 'alex_simpson@gmail.com'
    assert new_employee.phone == '11-12-1345'
    assert new_employee.position == 'chef'

def test_new_menu_item_with_fixture(new_menu_item):
    """
    GIVEN a MenuItem model
    WHEN a new MenuItem is created
    THEN check the menu_item_name, category_id, and price fields are defined correctly
    """
    assert new_menu_item.menu_item_name == 'cappuccino'
    assert new_menu_item.category_id == 3
    assert new_menu_item.price == 3.4

def test_new_order_with_fixture(new_order):
    """
    GIVEN a Order model
    WHEN a new Order is created
    THEN check the menu_item_id, customer_id, quantity, order_date and employee_id fields are defined correctly
    """
    assert new_order.menu_item_id == 1
    assert new_order.customer_id == 1
    assert new_order.quantity == 1
    assert new_order.order_date == '2024-01-21'
    assert new_order.employee_id == 1