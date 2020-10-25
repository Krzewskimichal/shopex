from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('create_product/', views.create_product, name='create_product'),
    path('categories_list/', views.CategoryList.as_view(), name='categories_list'),
    path('categories_detail/<int:pk>/', views.CategoriesDetail.as_view(), name='categories_detail'),
    path('subcategories_list/', views.SubCategoriesList.as_view(), name='subcategories_list'),
    path('subcategories_detail/<int:pk>/', views.SubCategoriesDetail.as_view(), name='subcategories_detail'),
]
