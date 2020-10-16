from rest_framework.serializers import ModelSerializer

from .models import Product, Categories, Subcategories


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class SubCategoriesSerializer(ModelSerializer):
    class Meta:
        model = Subcategories
        fields = '__all__'
