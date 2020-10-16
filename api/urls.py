from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('product-list/', views.product_list, name='product_list'),
    path('product-detail/<str:pk>/', views.product_detail, name='product_detail'),
]
