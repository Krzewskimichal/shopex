from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from shop.models import Product
from shop.serializers import ProductSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "Product List": "/product-list/",
        "Product detail": "/product-detail/<str:pk>/",
        "Create product": 'create-product/',
    }
    return Response(api_urls)


@api_view(['GET'])
def product_list(request):
    products = get_list_or_404(Product)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):

    try:
        product = get_object_or_404(Product, id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
