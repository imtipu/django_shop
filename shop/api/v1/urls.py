from django.urls import path
from .views import *


urlpatterns = [
    path('homepage/banner-sliders/', homepage_banner_sliders, name='api_home_banner_sliders'),
    path('home-categories/', home_categories, name='api_home_categories'),
    path('products/', ProductList.as_view(), name='api_product_list'),
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name='api_product_detail'),
    path('collections/<slug:slug>/', ProductCategoryDetailView.as_view(), name='api_collection_detail'),
    path('collections/<slug:slug>/products/', ProductCategoryProductList.as_view(), name='api_collection_products'),

    # cart urls
    path('cart/get-items/', cart_items_list, name='cart_items'),

]
