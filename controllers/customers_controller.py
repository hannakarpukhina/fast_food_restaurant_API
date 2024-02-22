from controllers.controller_helper import (
    add_element_from_json,
    get_element_by_id,
    get_element_by_query,
)
from models.customer import Customer


def display_customers():
    return get_element_by_query(Customer)


def insert_customer():
    return add_element_from_json(Customer)


def display_customer_name(id):
    return get_element_by_id(Customer, id)
