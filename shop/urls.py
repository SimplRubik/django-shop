
from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart-item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),
    
]
