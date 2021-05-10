from django.shortcuts import render
from rest_framework.response import Response

from django import views
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products
        pass

    def retrive(self, request, pk=None):  # /api/products/<string:id>
        pass

    def update(self, request, pk=None):  # /api/products/<string:id>
        pass

    def destroy(self, request, pk=None):  # /api/products/<string:id>
        pass
