from services.db_service import Model, DBService
import inspect
from sqlalchemy.orm.attributes import InstrumentedAttribute
import json

db_service = DBService()


class DBObject(Model):

    __abstract__ = True

    @classmethod
    def get_attribute_names(cls):
        column_list = []
        for member in inspect.getmembers(cls):
            if isinstance(
                member[1], InstrumentedAttribute
            ):  # and member[1].primary_key==False:
                column_list.append(member[0])
        return column_list

    def __repr__(self):
        output = {}
        column_names = self.get_attribute_names()
        for column_name in column_names:
            output[column_name] = getattr(self, column_name)
        return json.dumps(output)
