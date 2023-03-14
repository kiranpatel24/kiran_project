from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('bread/', bread, name='bread'),
    path('cart/', cart, name='cart'),
    path('drinks/', drinks, name='drinks'),
    path('events/', events, name='events'),
    path('faqs/', faqs, name='faqs'),
    path('frozen/', frozen, name='frozen'),
    path('household/', household, name='household'),
    path('index/', index, name='index'),
    path('kitchen/', kitchen, name='kitchen'),
    path('login/', login, name='login'),
    path('mail/', mail, name='mail'),
    path('payment/', payment, name='payment'),
    path('pet/', pet, name='pet'),
    path('privacy/', privacy, name='privacy'),
    path('products/', products, name='products'),
    path('services/', services, name='services'),
    path('shortcodes/', shortcodes, name='shortcodes'),
    path('single/', single, name='single'),
    path('vegetables/', vegetables, name='vegetables'),
    path('add_row/', add_row, name='add_row'),
    path('register/', register, name='register'),
    path('otp/', otp, name='otp'),
    path('logout/', logout, name='logout'),
    path('add_to_cart/<int:pk>',add_to_cart,name='add_to_cart'), 
    path('del_cart_item/<int:pk>',del_cart_item,name='del_cart_item'), 
    path('cart/paymenthandler/', paymenthandler, name='paymenthandler')

]