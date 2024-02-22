from models.db_object import DBObject, db_service
from dataclasses import dataclass


@dataclass
class Employee(DBObject):

    __tablename__ = "employee"

    db = db_service
    employee_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name: str = db.Column(db.String(100), primary_key=False)
    last_name: str = db.Column(db.String(100), primary_key=False)
    email: str = db.Column(db.String(100), primary_key=False)
    phone: str = db.Column(db.String(100), primary_key=False)
    position: str = db.Column(db.String(50), primary_key=False)
