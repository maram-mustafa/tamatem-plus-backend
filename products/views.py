from django.shortcuts import render
from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailsEditView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
