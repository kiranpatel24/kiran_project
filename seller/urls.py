from django.urls import path
from .views import *

urlpatterns = [
    path('seller_add_product/',seller_add_product, name='seller_add_product'),
    path('seller_edit_product/<int:pk>',seller_edit_product, name='seller_edit_product'),
    path('seller_index/',seller_index, name='seller_index'),
    path('seller_login/',seller_login, name='seller_login'),
    path('seller_products/',seller_products, name='seller_products'),
    path('seller_register/',seller_register, name='seller_register'),
    path('seller_otp/',seller_otp, name='seller_otp'),
    path('seller_logout/',seller_logout, name='seller_logout'),
    path('seller_edit_profile/',seller_edit_profile, name='seller_edit_profile'),
    path('product_delete/<int:pk>',product_delete, name='product_delete'),
#     path('order/',order, name='order'),
#     path('change_status/<int:pk>',change_status, name = 'change_status')
  ]