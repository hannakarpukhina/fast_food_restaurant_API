from models.db_object import DBObject, db_service
from dataclasses import dataclass
import datetime


@dataclass
class Order(DBObject):

    __tablename__ = "order"

    db = db_service
    order_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_item_id: int = db.Column(db.Integer, primary_key=False)
    customer_id: int = db.Column(db.Integer, primary_key=False)
    quantity: int = db.Column(db.Integer, primary_key=False)
    order_date: datetime = db.Column(db.Datetime, primary_key=False)
    employee_id: int = db.Column(db.Integer, primary_key=False)
