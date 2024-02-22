from controllers.controller_helper import (
    add_element_from_json,
    get_element_by_id,
    get_element_by_query,
)
from models.order import Order


def display_orders():
    return get_element_by_query(Order)


def insert_order():
    return add_element_from_json(Order)


def display_order_details(id):
    return get_element_by_id(Order, id)
