from tests.static.elements import (
    category_attributes,
    customer_attributes,
    employee_attributes,
    menu_item_attributes,
    order_attributes,
)


def test_new_category(new_category):
    """
    GIVEN a Category model
    WHEN a new Category is created
    THEN check the category_name, active, and parent_category_id fields are defined correctly
    """
    assert new_category.category_name == category_attributes["category_name"]
    assert new_category.active == category_attributes["active"]
    assert new_category.parent_category_id == category_attributes["parent_category_id"]


def test_new_customer(new_customer):
    """
    GIVEN a Customer model
    WHEN a new Customer is created
    THEN check the first_name, last_name, and email fields are defined correctly
    """
    assert new_customer.first_name == customer_attributes["first_name"]
    assert new_customer.last_name == customer_attributes["last_name"]
    assert new_customer.email == customer_attributes["email"]


def test_new_employee(new_employee):
    """
    GIVEN a Employee model
    WHEN a new Employee is created
    THEN check the first_name, last_name, email, phone and position fields are defined correctly
    """
    assert new_employee.first_name == employee_attributes["first_name"]
    assert new_employee.last_name == employee_attributes["last_name"]
    assert new_employee.email == employee_attributes["email"]
    assert new_employee.phone == employee_attributes["phone"]
    assert new_employee.position == employee_attributes["position"]


def test_new_menu_item(new_menu_item):
    """
    GIVEN a MenuItem model
    WHEN a new MenuItem is created
    THEN check the menu_item_name, category_id and price fields are defined correctly
    """
    assert new_menu_item.menu_item_name == menu_item_attributes["menu_item_name"]
    assert new_menu_item.category_id == menu_item_attributes["category_id"]
    assert new_menu_item.price == menu_item_attributes["price"]


def test_new_order(new_order):
    """
    GIVEN a Order model
    WHEN a new Order is created
    THEN check the menu_item_id, customer_id, quantity, order_date and employee_id fields are defined correctly
    """
    assert new_order.menu_item_id == order_attributes["menu_item_id"]
    assert new_order.customer_id == order_attributes["customer_id"]
    assert new_order.quantity == order_attributes["quantity"]
    assert new_order.order_date == order_attributes["order_date"]
    assert new_order.employee_id == order_attributes["employee_id"]


def test_attribute_names(attribute_names):
    assert attribute_names == sorted(
        ["category_id", "category_name", "active", "parent_category_id"]
    )
