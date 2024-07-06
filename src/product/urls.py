from django.urls import path

from .views import *

urlpatterns = [
    path('show/<int:id>/', show, name='show'),
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('shop/show/<int:id>/', show, name='show'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('about/', about, name='about'),
]
