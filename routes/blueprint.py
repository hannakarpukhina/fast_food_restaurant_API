from flask import Blueprint
from controllers.food_order_controller import (
    insert_categories,
    get_categories,
    get_category_by_id,
    insert_menu_items,
    get_menu_items,
    get_menu_item_by_id,
    insert_customers,
    get_customers,
    get_customer_by_id,
    insert_employees,
    get_employees,
    get_employee_by_id,
    insert_orders,
    get_orders,
    get_order_by_id,
    delete_category_by_id,
    delete_customer_by_id,
    delete_employee_by_id,
    delete_menu_item_by_id,
    delete_order_by_id,
)


blueprint = Blueprint("blueprint", __name__)


blueprint.route("/categories", methods=["POST"])(insert_categories)
blueprint.route("/categories", methods=["GET"])(get_categories)
blueprint.route("/categories/<id>", methods=["GET"])(get_category_by_id)
blueprint.route("/categories/<id>", methods=["DELETE"])(delete_category_by_id)

blueprint.route("/menu_items", methods=["POST"])(insert_menu_items)
blueprint.route("/menu_items", methods=["GET"])(get_menu_items)
blueprint.route("/menu_items/<id>", methods=["GET"])(get_menu_item_by_id)
blueprint.route("/menu_items/<id>", methods=["DELETE"])(delete_menu_item_by_id)

blueprint.route("/customers", methods=["POST"])(insert_customers)
blueprint.route("/customers", methods=["GET"])(get_customers)
blueprint.route("/customers/<id>", methods=["GET"])(get_customer_by_id)
blueprint.route("/customers/<id>", methods=["DELETE"])(delete_customer_by_id)

blueprint.route("/employees", methods=["POST"])(insert_employees)
blueprint.route("/employees", methods=["GET"])(get_employees)
blueprint.route("/employees/<id>", methods=["GET"])(get_employee_by_id)
blueprint.route("/employees/<id>", methods=["DELETE"])(delete_employee_by_id)

blueprint.route("/orders", methods=["POST"])(insert_orders)
blueprint.route("/orders", methods=["GET"])(get_orders)
blueprint.route("/orders/<id>", methods=["GET"])(get_order_by_id)
blueprint.route("/orders/<id>", methods=["DELETE"])(delete_order_by_id)
