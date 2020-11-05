from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from shop.models import Product, Categories, Subcategories
from shop.serializers import ProductSerializer, CategoriesSerializer, SubCategoriesSerializer


# function Product api_view(for learning)
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "Product List": "/product_list/",
        "Product detail": "/product_detail/<str:pk>/",
        "Categories list": "/categories_list/",
        "Categories detail": "/categories_detail/<str:pk>/",
        "Subcategories list": "/subcategories_list/",
        "Subcategories detail": "/subcategories_detail/<str:pk>/",
    }
    return Response(api_urls)


# @api_view(['GET'])
# def product_list(request):
#     products = get_list_or_404(Product)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#
#     try:
#         product = get_object_or_404(Product, id=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = ProductSerializer(product, many=False)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['POST'])
# def create_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)


class CategoryList(APIView):

    def get(self, request):
        category = Categories.objects.all()
        serializer = CategoriesSerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CategoriesDetail(APIView):

    def get(self, request, pk):
        category = get_object_or_404(Categories, id=pk)
        serializer = CategoriesSerializer(category, many=False)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        category = get_object_or_404(Categories, id=pk)
        serializer = CategoriesSerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Categories, id=pk)
        category.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class SubCategoriesList(generics.ListCreateAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubCategoriesSerializer


class SubCategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubCategoriesSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
