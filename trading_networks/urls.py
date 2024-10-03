from django.urls import path

from trading_networks.api_views.api_network import NetworkCreateAPIView, NetworkListAPIView, NetworkRetrieveAPIView, \
    NetworkUpdateAPIView, NetworkDestroyAPIView, NetworkDebtAverageAPIView, NetworkByProductAPIView, \
    GenerateQrCodeAPIView
from trading_networks.apps import TradingNetworksConfig

app_name = TradingNetworksConfig.name

urlpatterns = [
    path('create/', NetworkCreateAPIView.as_view(), name='network-create'),
    path('list/', NetworkListAPIView.as_view(), name='network-list'),
    path('detail/<int:pk>/', NetworkRetrieveAPIView.as_view(), name='network-detail'),
    path('update/<int:pk>/', NetworkUpdateAPIView.as_view(), name='network-update'),
    path('delete/<int:pk>/', NetworkDestroyAPIView.as_view(), name='network-delete'),

    path('debt-exceeds-average/', NetworkDebtAverageAPIView.as_view(), name='network-debt-exceeds-average'),
    path('product/<int:product_id>/', NetworkByProductAPIView.as_view(), name='network-by-product'),

    path('generate-qr/<int:network_id>/', GenerateQrCodeAPIView.as_view(), name='generate-qr-code'),

]
