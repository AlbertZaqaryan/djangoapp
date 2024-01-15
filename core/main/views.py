from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductViews(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
