from django.urls import path


from .views import Index, ProductList

app_name = 'shop'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('/<str:gender>/', ProductList.as_view(), name='product_list'),
]
