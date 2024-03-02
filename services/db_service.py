from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Float, Boolean, Column, DateTime

DB = SQLAlchemy()
Model = DB.Model


class DBService:
    def __init__(self):

        self.db = DB

        self.String = String
        self.Integer = Integer
        self.Float = Float
        self.Boolean = Boolean
        self.Datetime = DateTime
        self.Column = Column

    def insert_object_into_db(self, instance):
        self.db.session.add(instance)
        self.db.session.commit()

    def get_object_query_from_db(self, model):
        return self.db.session.query(model)
    
    def delete_object_from_db(self, instance):
        self.db.session.delete(instance)
        self.db.session.commit()
