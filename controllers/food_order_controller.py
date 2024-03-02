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
                    raise KeyError(f'Attribute "{incorected_attr}" is not supported')

        column_values = {}
        for column in model.get_attribute_names():
            if column in request_json:
                column_values[column] = request_json[column]

        instance = model(**column_values)
        db_service.insert_object_into_db(instance)

        result = {"result": instance}
        return result

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


def delete_element_by_id(model: DBObject, id):
    element = db_service.get_object_query_from_db(model).get_or_404(id)
    db_service.delete_object_from_db(element)
    result = {"result": element}
    return f"Element with id = {id} was successfully deleted"


def get_categories():
    return get_element_by_query(Category)


def insert_categories():
    return add_element_from_json(Category)


def get_category_by_id(id):
    return get_element_by_id(Category, id)


def delete_category_by_id(id):
    return delete_element_by_id(Category, id)


def get_customers():
    return get_element_by_query(Customer)


def insert_customers():
    return add_element_from_json(Customer)


def get_customer_by_id(id):
    return get_element_by_id(Customer, id)


def delete_customer_by_id(id):
    return delete_element_by_id(Customer, id)


def get_employees():
    return get_element_by_query(Employee)


def insert_employees():
    return add_element_from_json(Employee)


def get_employee_by_id(id):
    return get_element_by_id(Employee, id)


def delete_employee_by_id(id):
    return delete_element_by_id(Employee, id)


def get_menu_items():
    return get_element_by_query(MenuItem)


def insert_menu_items():
    return add_element_from_json(MenuItem)


def get_menu_item_by_id(id):
    return get_element_by_id(MenuItem, id)


def delete_menu_item_by_id(id):
    return delete_element_by_id(MenuItem, id)


def get_orders():
    return get_element_by_query(Order)


def insert_orders():
    return add_element_from_json(Order)


def get_order_by_id(id):
    return get_element_by_id(Order, id)


def delete_order_by_id(id):
    return delete_element_by_id(Order, id)
