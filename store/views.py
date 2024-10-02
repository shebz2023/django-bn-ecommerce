from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import productSerializer

# Create your views here.


@api_view()
def product_list(request):
    products = Product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)


@api_view()
def singleProduct(request, id):
    try:
        product = Product.objects.get(id=id)
        serializer = productSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
