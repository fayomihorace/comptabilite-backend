import graphene
from .types import ProductType, RecordType
from .models import Product, Record
from .mutations import ProductMutation, RecordMutation


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    records = graphene.List(RecordType)
    
    search = graphene.Field(RecordType, product_id=graphene.String())#, name=graphene.String())
    
    def resolve_search(self, info, product_id):
        return Record.objects.get(product_id="5e32f0a4f2a5e3b9e1e3c1a7")
     
    def resolve_products(self, info):
    	return list(Product.objects.all())
 
    def resolve_records(self, info):
    	return list(Record.objects.all())


class Mutation(graphene.ObjectType):
    product_mutation = ProductMutation.Field()
    record_mutation  = RecordMutation.Field()

