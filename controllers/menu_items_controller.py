from controllers.controller_helper import (
    add_element_from_json,
    get_element_by_id,
    get_element_by_query,
)
from models.menu_item import MenuItem


def display_menu_items():
    return get_element_by_query(MenuItem)


def insert_menu_item():
    return add_element_from_json(MenuItem)


def display_menu_item_name(id):
    return get_element_by_id(MenuItem, id)
