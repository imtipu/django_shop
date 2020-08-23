from django.shortcuts import render
from django.views.generic import *

from shop.models import *
# Create your views here.


def admin_dashboard(request):
    data = {
        'title': 'Dashboard'
    }
    return render(request, 'admin/dashboard/home.html', data)


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'admin/dashboard/products/product_list.html'
