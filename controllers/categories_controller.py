from controllers.controller_helper import (
    add_element_from_json,
    get_element_by_id,
    get_element_by_query,
)
from models.category import Category


def display_categories():
    return get_element_by_query(Category)


def insert_categories():
    return add_element_from_json(Category)


def display_category_name(id):
    return get_element_by_id(Category, id)
