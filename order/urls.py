from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order', views.add_product_to_order, name='add-product-to-order'),
    path('payment', views.payment_start, name='payment_start'),
    path('payment/return', views.payment_return, name='payment_return'),
]
