from models.db_object import DBObject, db_service
from dataclasses import dataclass


@dataclass
class Category(DBObject):

    __tablename__ = "category"

    db = db_service
    category_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name: str = db.Column(db.String(100), primary_key=False)
    active: bool = db.Column(db.Boolean, primary_key=False)
    parent_category_id: int = db.Column(db.Integer, primary_key=False, nullable=True)
