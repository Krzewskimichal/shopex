from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from .models import Product


class Index(TemplateView):
    template_name = 'shop/index.html'


class ProductList(View):

    def get(self, request, gender):
        products = Product.objects.filter(gender=gender)
        context = {'products': products, 'gender': gender}
        return render(request, 'shop/product_list.html', context)
