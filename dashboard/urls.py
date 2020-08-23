from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', admin_dashboard, name='dashboard_home'),
    path('products/', ProductList.as_view(), name='admin_products'),
]
