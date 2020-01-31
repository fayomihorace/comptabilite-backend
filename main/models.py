from mongoengine import Document
from mongoengine.fields import StringField, FloatField, ObjectIdField, IntField


class Product(Document):
    meta = {'collection': 'products'}
    ID = ObjectIdField()
    name = StringField(required=True)
    volume = FloatField(required=True)
    

class Record(Document):
    meta = {'collection': 'record'}
    ID = ObjectIdField()
    product_id = StringField()
    stock_in   = IntField()
    stock_out  = IntField()
    buy_price   = FloatField()
    sell_price  = FloatField()
    
    day        = IntField()
    month      = StringField()
    year       = IntField()
    

class DayBilan(Document):
    meta = {'collection': 'dayBilan'}
    day        = IntField()
    month      = StringField()
    year       = IntField()
    money_in   = IntField()
    money_out  = IntField()
    