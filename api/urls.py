from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('categories_list/', views.CategoryList.as_view(), name='categories_list'),
    path('categories_detail/<int:pk>/', views.CategoriesDetail.as_view(), name='categories_detail'),
    path('subcategories_list/', views.SubCategoriesList.as_view(), name='subcategories_list'),
    path('subcategories_detail/<int:pk>/', views.SubCategoriesDetail.as_view(), name='subcategories_detail'),
]
