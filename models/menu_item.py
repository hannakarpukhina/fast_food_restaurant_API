from models.db_object import DBObject, db_service
from dataclasses import dataclass


@dataclass
class MenuItem(DBObject):

    __tablename__ = "menu_item"

    db = db_service
    menu_item_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_item_name: str = db.Column(db.String(100), primary_key=False)
    category_id: int = db.Column(db.Integer, primary_key=False)
    price: float = db.Column(db.Float, primary_key=False)
