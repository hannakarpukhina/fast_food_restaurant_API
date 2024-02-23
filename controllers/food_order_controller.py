from models.category import Category
from models.customer import Customer
from models.employee import Employee
from models.menu_item import MenuItem
from models.order import Order
from models.db_object import DBObject
from services.db_service import DBService
from flask import request
from sqlalchemy import exc


db_service = DBService()


def add_element_from_json(model: DBObject):

    try:
        json = request.json
        if type(json) == dict:
            json = [json]
        elif type(json) != list:
            raise TypeError()
        for request_json in json:
            for json_param in request_json:
                if json_param not in model.get_attribute_names():
                    incorected_attr = json_param
                    raise KeyError(f'attribute "{incorected_attr}" is not supported')

        column_values = {}
        for column in model.get_attribute_names():
            if column in request_json:
                column_values[column] = request_json[column]

        instance = model(**column_values)
        db_service.insert_object_into_db(instance)

        return "new elements is added"

    except exc.IntegrityError as e:
        return str(e.orig).split(":")[-1].replace("\n", "").strip(), 409

    except KeyError as err:
        return str(err), 400


def get_element_by_id(model: DBObject, id):
    element = db_service.get_object_query_from_db(model).get_or_404(id)
    result = {"result": element}
    return result


def get_element_by_query(model: DBObject):
    param_list = list(request.args.items())
    error_message = ""
    incorrect_param = []
    query = db_service.get_object_query_from_db(model)
    if len(param_list) > 0:
        for key, value in request.args.items():
            try:
                query = query.filter(getattr(model, key) == value)
            except AttributeError:
                incorrect_param.append(key)
        error_message = (
            f"Query param {incorrect_param} is not supported and ignored by the query."
        )
    elements = query.all()
    output = []
    for element in elements:
        output.append(element)

    result = {"result": output}

    if len(incorrect_param) > 0:
        result["warning"] = error_message

    return result


def display_categories():
    return get_element_by_query(Category)


def insert_categories():
    return add_element_from_json(Category)


def display_category_name(id):
    return get_element_by_id(Category, id)


def display_customers():
    return get_element_by_query(Customer)


def insert_customer():
    return add_element_from_json(Customer)


def display_customer_name(id):
    return get_element_by_id(Customer, id)


def display_employees():
    return get_element_by_query(Employee)


def insert_employee():
    return add_element_from_json(Employee)


def display_employee_name(id):
    return get_element_by_id(Employee, id)


def display_menu_items():
    return get_element_by_query(MenuItem)


def insert_menu_item():
    return add_element_from_json(MenuItem)


def display_menu_item_name(id):
    return get_element_by_id(MenuItem, id)


def display_orders():
    return get_element_by_query(Order)


def insert_order():
    return add_element_from_json(Order)


def display_order_details(id):
    return get_element_by_id(Order, id)
