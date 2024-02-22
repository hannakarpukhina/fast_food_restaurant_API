from controllers.controller_helper import (
    add_element_from_json,
    get_element_by_id,
    get_element_by_query,
)
from models.employee import Employee


def display_employees():
    return get_element_by_query(Employee)


def insert_employee():
    return add_element_from_json(Employee)


def display_employee_name(id):
    return get_element_by_id(Employee, id)
