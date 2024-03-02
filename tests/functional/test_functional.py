import json
from services.db_service import DBService
from tests.static.elements import (
    category_attributes,
    customer_attributes,
    employee_attributes,
    menu_item_attributes,
    order_attributes,
)

db_service = DBService()

def test_category_get_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/categories' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/categories")
    assert response.status_code == 200


def test_customer_get_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/customers' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/customers")
    assert response.status_code == 200


def test_employee_get_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/employees' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/employees")
    assert response.status_code == 200


def test_menu_item_get_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/menu_items' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/menu_items")
    assert response.status_code == 200


def test_order_get_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/orders' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/orders")
    assert response.status_code == 200


def test_category_post_request_unsupported_format(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/categories' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = client.post("/categories")
    assert response.status_code == 415


def test_customer_post_request_unsupported_format(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/customers' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = client.post("/customers")
    assert response.status_code == 415


def test_emoloyee_post_request_unsupported_format(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/employees' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = client.post("/employees")
    assert response.status_code == 415


def test_menu_item_post_request_unsupported_format(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/menu_items' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = client.post("/menu_items")
    assert response.status_code == 415


def test_order_post_request_unsupported_format(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/orders' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """
    response = client.post("/orders")
    assert response.status_code == 415

    
def test_category_post_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/categories' pages is posted to (POST)
    THEN check that a '200' (The media format of the requested data is supported by the server) status code is returned
         and delete the test data from the server
    """
    response = client.post(
        "/categories",
        data=json.dumps(category_attributes),
        content_type="application/json",
    )
    assert response.status_code == 200

    id = 0
    for i in response.json["result"]:
        if i == "category_id":
            id = response.json["result"]["category_id"]
            break

    delete_response = client.delete(f"/categories/{id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/categories/{id}")
    assert get_response.status_code == 404


def test_customer_post_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/customers' pages is posted to (POST)
    THEN check that a '200' (The media format of the requested data is supported by the server) status code is returned
         and delete the test data from the server
    """
    response = client.post(
        "/customers",
        data=json.dumps(customer_attributes),
        content_type="application/json",
    )
    assert response.status_code == 200

    id = 0
    for i in response.json["result"]:
        if i == "customer_id":
            id = response.json["result"]["customer_id"]
            break

    delete_response = client.delete(f"/customers/{id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/customers/{id}")
    assert get_response.status_code == 404


def test_employee_post_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/employees' pages is posted to (POST)
    THEN check that a '200' (The media format of the requested data is supported by the server) status code is returned
         and delete the test data from the server
    """
    response = client.post(
        "/employees",
        data=json.dumps(employee_attributes),
        content_type="application/json",
    )
    assert response.status_code == 200

    id = 0
    for i in response.json["result"]:
        if i == "employee_id":
            id = response.json["result"]["employee_id"]
            break

    delete_response = client.delete(f"/employees/{id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/employees/{id}")
    assert get_response.status_code == 404


def test_menu_item_post_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/menu_items' pages is posted to (POST)
    THEN check that a '200' (The media format of the requested data is supported by the server) status code is returned
         and delete the test data from the server
    """
    response = client.post(
        "/menu_items",
        data=json.dumps(menu_item_attributes),
        content_type="application/json",
    )
    assert response.status_code == 200

    id = 0
    for i in response.json["result"]:
        if i == "menu_item_id":
            id = response.json["result"]["menu_item_id"]
            break

    delete_response = client.delete(f"/menu_items/{id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/menu_items/{id}")
    assert get_response.status_code == 404


def test_order_post_request(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/orders' pages is posted to (POST)
    THEN check that a '200' (The media format of the requested data is supported by the server) status code is returned
         and delete the test data from the server
    """
    response = client.post(
        "/orders",
        data=json.dumps(order_attributes),
        content_type="application/json",
    )
    assert response.status_code == 200

    id = 0
    for i in response.json["result"]:
        if i == "order_id":
            id = response.json["result"]["order_id"]
            break

    delete_response = client.delete(f"/orders/{id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/orders/{id}")
    assert get_response.status_code == 404
