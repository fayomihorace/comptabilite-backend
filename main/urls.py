from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 	path('product', views.productView.as_view()),
]

"""path('product/name', views.productNameView.as_view()),
   	path('product/category', views.productCategoryView.as_view()),"""