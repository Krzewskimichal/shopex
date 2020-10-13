from django.contrib import admin

from .models import Categories, Product, Subcategories, Brand, ProductsSizes
admin.site.register(Categories)
admin.site.register(ProductsSizes)
admin.site.register(Product)
admin.site.register(Subcategories)
admin.site.register(Brand)
