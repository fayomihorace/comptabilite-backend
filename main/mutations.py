import graphene
from .types import ProductType, RecordType, DayBilanType
from .models import Product, Record, DayBilan


class ProductMutation(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        name = graphene.String()
        volume = graphene.Float()

    def mutate(self, info, name, volume):
        product = Product(
            name=name,
            volume=volume,
        )
        product.save()

        return ProductMutation(product=product)



class RecordMutation(graphene.Mutation):
    record = graphene.Field(RecordType)

    class Arguments:
        product_id = graphene.String() 
        day        = graphene.Int()
        month      = graphene.String()
        year       = graphene.Int()
        
        stock_in   = graphene.Int()
        stock_out  = graphene.Int()
        buy_price  = graphene.Float()
        sell_price = graphene.Float()

    def mutate(self, info, product_id, day, month, year, stock_in, stock_out, buy_price, sell_price):
        
        exist = Record.objects.filter(product_id=product_id, day=day, month=month, year=year)
        if( len(exist)==0 ):
            record = Record(
                product_id = product_id,
                day        = day,
                month      = month,
                year       = year,
                stock_in   = stock_in,
                stock_out  = stock_out,
                buy_price  = buy_price,
                sell_price = sell_price,
            )
            record.save()

            return RecordMutation(record=record)
        else:
            record=exist[0]
            record.stock_in=stock_in
            record.stock_out=stock_out
            record.buy_price=buy_price
            record.sell_price=sell_price
            raise Exception('Record updated')



class DayBilanMutation(graphene.Mutation):
    day_bilan = graphene.Field(RecordType)

    class Arguments: 
        day        = graphene.Int()
        month      = graphene.String()
        year       = graphene.Int()
        

    def mutate(self, info, day, month, year, money_in, money_out):        
        pass
