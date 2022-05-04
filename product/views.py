from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from product.models import ProductCategory


from .serializers import  ProductCategorySerializer
from .serializers import  ProductSerializer

class ProductList(APIView):
    
    def get(self, request):
        product1 = Product.objects.all()
        serializer = ProductSerializer(product1, many = True)
        return Response(serializer.data)

    def post(self):
        pass

class ProductCategoryList(APIView):
    
    def get(self, request):
        prodcutcategory1 = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(prodcutcategory1, many = True)
        return Response(serializer.data)

    def post(self):
        pass