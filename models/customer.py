from models.db_object import DBObject, db_service
from dataclasses import dataclass


@dataclass
class Customer(DBObject):

    __tablename__ = "customer"

    db = db_service
    customer_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name: str = db.Column(db.String(100), primary_key=False, nullable=True)
    last_name: str = db.Column(db.String(100), primary_key=False, nullable=True)
    email: str = db.Column(db.String(100), primary_key=False, nullable=True)
