import graphene
from graphene_mongo import MongoengineObjectType
from .models import Product, Record, DayBilan


class ProductType(MongoengineObjectType):
    class Meta:
        model = Product
        

class RecordType(MongoengineObjectType):
    class Meta:
        model = Record
        
        
class DayBilanType(MongoengineObjectType):
    class Meta:
        model = DayBilan
        