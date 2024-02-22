from flask import Blueprint
from controllers.categories_controller import (
    insert_categories,
    display_categories,
    display_category_name,
)
from controllers.menu_items_controller import (
    insert_menu_item,
    display_menu_items,
    display_menu_item_name,
)
from controllers.customers_controller import (
    insert_customer,
    display_customers,
    display_customer_name,
)
from controllers.employees_controller import (
    insert_employee,
    display_employees,
    display_employee_name,
)
from controllers.orders_controller import (
    insert_order,
    display_orders,
    display_order_details,
)


blueprint = Blueprint("blueprint", __name__)


def index():
    return "first empty page"


blueprint.route("/", methods=["GET"])(index)
blueprint.route("/categories", methods=["POST"])(insert_categories)
blueprint.route("/categories/<id>", methods=["GET"])(display_category_name)
blueprint.route("/categories", methods=["GET"])(display_categories)

blueprint.route("/menu_items", methods=["POST"])(insert_menu_item)
blueprint.route("/menu_items", methods=["GET"])(display_menu_items)
blueprint.route("/menu_items/<id>", methods=["GET"])(display_menu_item_name)

blueprint.route("/customers", methods=["POST"])(insert_customer)
blueprint.route("/customers", methods=["GET"])(display_customers)
blueprint.route("/customers/<id>", methods=["GET"])(display_customer_name)

blueprint.route("/employees", methods=["POST"])(insert_employee)
blueprint.route("/employees", methods=["GET"])(display_employees)
blueprint.route("/employees/<id>", methods=["GET"])(display_employee_name)

blueprint.route("/orders", methods=["POST"])(insert_order)
blueprint.route("/orders", methods=["GET"])(display_orders)
blueprint.route("/orders/<id>", methods=["GET"])(display_order_details)
