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
        pass

    def update(self, request):
        pass


class productNameView(AccessMixin, View):
    
    def get(self, request):
        pass


class productCategoryView(AccessMixin, View):
    
    def get(self, request):
        pass

class testView(AccessMixin, View):
    
    def get(self, request):
        pass
