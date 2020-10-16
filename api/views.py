from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop.models import Product
from shop.serializers import ProductSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "Product List": "/product-list/",
        "Product detail": "/product-detail/<str:pk>/"
    }
    return Response(api_urls)


@api_view(['GET'])
def product_list(request):
    products = get_list_or_404(Product)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
