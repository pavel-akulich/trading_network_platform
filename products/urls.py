from django.urls import path

from products.api_views.api_product import ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('list/', ProductListAPIView.as_view(), name='product-list'),
    path('detail/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product-delete'),
]
