from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import AccessMixin #LoginRequiredMixin, 
from pymongo import MongoClient
import pprint

client= MongoClient('mongodb://localhost:27017/')
db=client.comptabilite
# Create your views here.
class productView(AccessMixin, View):
     
    def get(self, request):
        #db.product_name.insert_one({'name': "Flag", 'volume':0.33})
        #product_names=db.product_name.find({})
        result = []
        for p in db.product_name.find(): result.append(p)
        print(result[0])
        return HttpResponse( result[0]["_id"] )
    
    def update(self, request):
        product_names=db.product_name.find()
        return HttpResponse(product_names[0] )


class productNameView(AccessMixin, View):
    
    def get(self, request):
        client= MongoClient('mongodb://localhost:27017/')
        db=client.comptabilite
        product_table=db.comptabilite    
        #new_product=product_table.insert_one({'name': "Flag", 'volume':0.33})
        #inserted_id=new_product.inserted_id
        collection_list_names=db.list_collection_names()
        return HttpResponse(collection_list_names)


class productCategoryView(AccessMixin, View):
    
    def get(self, request):
        client= MongoClient('mongodb://localhost:27017/')
        db=client.comptabilite
        product_table=db.comptabilite    
        #new_product=product_table.insert_one({'name': "Flag", 'volume':0.33})
        #inserted_id=new_product.inserted_id
        collection_list_names=db.list_collection_names()
        return HttpResponse(collection_list_names)

class testView(AccessMixin, View):
    
    def get(self, request):
        client= MongoClient('mongodb://localhost:27017/')
        db=client.comptabilite
        product_table=db.comptabilite    
        #new_product=product_table.insert_one({'name': "Flag", 'volume':0.33})
        #inserted_id=new_product.inserted_id
        collection_list_names=db.list_collection_names()
        return HttpResponse(collection_list_names)
